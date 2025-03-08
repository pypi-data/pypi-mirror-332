import qtility
import factories
from Qt import QtCore, QtWidgets


class FactoryWidget(QtWidgets.QWidget):

    def __init__(self, factory: factories.Factory, horizontal=False, parent=None):
        super(FactoryWidget, self).__init__(parent=parent)

        # -- We cannot be flexible on this, we need to ensure the
        # -- incoming factory argument is indeed a factory!
        if not isinstance(factory, factories.Factory):
            raise Exception("factory must be a factories.Factory instance")

        # -- Store our factory reference
        self._factory = factory
        self._plugin_editor = PluginEditor(factory=self._factory)
        self._path_editor = PathEditor(factory=self._factory)

        layout_type = QtWidgets.QVBoxLayout
        if horizontal:
            layout_type = QtWidgets.QHBoxLayout

        # -- Create our master layout
        self.setLayout(
            qtility.layouts.slimify(
                layout_type(),
            ),
        )

        self.plugin_groupbox = QtWidgets.QGroupBox("Plugins")
        self.plugin_groupbox.setLayout(
            QtWidgets.QVBoxLayout(),
        )
        self.plugin_groupbox.layout().addWidget(self._plugin_editor)

        self.path_groupbox = QtWidgets.QGroupBox("Paths")
        self.path_groupbox.setLayout(
            QtWidgets.QVBoxLayout(),
        )
        self.path_groupbox.layout().addWidget(self._path_editor)

        self.layout().addWidget(self.plugin_groupbox)
        self.layout().addWidget(self.path_groupbox)

    @property
    def factory(self) -> factories.Factory:
        """
        Read only property accessor for the factory
        """
        return self._factory


class PluginEditor(QtWidgets.QWidget):

    changed = QtCore.Signal()

    def __init__(self, factory: factories.Factory, parent=None):
        super(PluginEditor, self).__init__(parent=parent)

        # -- We cannot be flexible on this, we need to ensure the
        # -- incoming factory argument is indeed a factory!
        if not isinstance(factory, factories.Factory):
            raise Exception("factory must be a factories.Factory instance")

        # -- Store our factory reference
        self._factory = factory
        self._current_row = 0

        # -- Create our master layout
        self.setLayout(
            qtility.layouts.slimify(
                QtWidgets.QVBoxLayout(),
            ),
        )

        # -- Create the main list widget
        self.plugin_list = QtWidgets.QListWidget()
        self.layout().addWidget(self.plugin_list)

        # -- Create the add and remove buttons
        self.enable_button = QtWidgets.QPushButton("Enable")
        self.disable_button = QtWidgets.QPushButton('Disable')
        self.debug_button = QtWidgets.QPushButton('Debug')

        # -- Create the button layout
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.enable_button)
        button_layout.addWidget(self.disable_button)
        self.layout().addLayout(button_layout)

        # -- Populate our view
        self.populate_plugin_list()

        # -- Hook up our signals and slots
        self._factory.plugins_changed.connect(self.populate_plugin_list)
        self.enable_button.clicked.connect(self.enable_plugins)
        self.disable_button.clicked.connect(self.disable_plugins)

    def enable_plugins(self):

        # -- Get the items
        items = self.plugin_list.selectedItems()
        self._current_row = self.plugin_list.currentRow()

        # -- If there are no items then we do not need to request for
        # -- anything to be run
        if not items:
            return

        for item in items:
            self.factory.set_disabled(
                item.identifier,
                False,
            )

    def disable_plugins(self):

        # -- Get the items
        items = self.plugin_list.selectedItems()
        self._current_row = self.plugin_list.currentRow()

        # -- If there are no items then we do not need to request for
        # -- anything to be run
        if not items:
            return

        for item in items:
            self.factory.set_disabled(
                item.identifier,
                True,
            )

    def populate_plugin_list(self):

        # -- Clear the list before re-adding
        self.plugin_list.clear()

        # -- Cycle the paths and add them back in. Set the tooltip as
        # -- the path because they can be quite long
        for identifier in sorted(self.factory.identifiers(include_disabled=True)):

            # -- For the label we want to show the identifier and the
            # -- state
            label = identifier
            if self.factory.is_disabled(identifier):
                label += " (Disabled)"

            # -- Add the item, but include the identifier too
            item = QtWidgets.QListWidgetItem(label)
            item.identifier = identifier
            self.plugin_list.addItem(item)

        self.plugin_list.setCurrentRow(self._current_row)

    @property
    def factory(self) -> factories.Factory:
        """
        Read only property accessor for the factory
        """
        return self._factory


class PathEditor(QtWidgets.QWidget):

    changed = QtCore.Signal()

    def __init__(self, factory: factories.Factory, parent=None):
        super(PathEditor, self).__init__(parent=parent)

        # -- We cannot be flexible on this, we need to ensure the
        # -- incoming factory argument is indeed a factory!
        if not isinstance(factory, factories.Factory):
            raise Exception("factory must be a factories.Factory instance")

        # -- Store our factory reference
        self._factory = factory

        # -- Create our master layout
        self.setLayout(
            qtility.layouts.slimify(
                QtWidgets.QVBoxLayout(),
            ),
        )

        # -- Create the main list widget
        self.path_list = QtWidgets.QListWidget()
        self.layout().addWidget(self.path_list)

        # -- Create the add and remove buttons
        self.add_button = QtWidgets.QPushButton("Add")
        self.remove_button = QtWidgets.QPushButton('Remove')

        # -- Create the button layout
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        self.layout().addLayout(layout)


        # -- Populate our view
        self.populate_path_list()

        # -- Hook up our signals and slots
        self._factory.paths_changed.connect(self.populate_path_list)
        self.add_button.clicked.connect(self.add_path)
        self.remove_button.clicked.connect(self.remove_path)

    def add_path(self):

        # -- Use the first path in the list as the starting point
        # -- for the folder browser if possible
        try:
            start_path = self.factory.paths()[0]
        except IndexError:
            start_path = ""

        # -- Ask the user for the path to add
        path_to_add = qtility.request.folderpath(
            title="Select Path",
            path=start_path,
            parent=self,
        )

        # -- If the user cancelled, then we do not need
        # -- to continue
        if not path_to_add:
            return

        # -- Add the path to the factory. This will emit a
        # -- path change which will automatically refresh
        # -- this widget
        self.factory.add_path(
            path_to_add.replace("\\", "/"),
        )

    def remove_path(self):

        # -- Get the items
        items = self.path_list.selectedItems()

        # -- If there are no items then we do not need to request for
        # -- anything to be run
        if not items:
            return

        # -- Get the actual text for the paths
        paths_to_remove = [
            item.text()
            for item in items
        ]

        # -- Lets double check that the user really does want
        # -- to remove these paths
        message = "Are you sure you want to remove %s paths?" % len(paths_to_remove)
        confirmation = qtility.request.confirmation(
            title="Remove Plugin Paths",
            message=message,
            parent=self,
        )

        if not confirmation:
            return

        # -- Cycle the paths and remove them. Note that we do not
        # -- need to force a refresh, as the factory will emit a
        # -- change signal which will automatically refresh this
        # -- widget
        for path in paths_to_remove:
            self.factory.remove_path(path)

    def populate_path_list(self):

        # -- Clear the list before re-adding
        self.path_list.clear()

        # -- Cycle the paths and add them back in. Set the tooltip as
        # -- the path because they can be quite long
        for path in sorted(self.factory.paths()):
            item = QtWidgets.QListWidgetItem(path)
            item.setToolTip(path)
            self.path_list.addItem(item)

    @property
    def factory(self) -> factories.Factory:
        """
        Read only property accessor for the factory
        """
        return self._factory
