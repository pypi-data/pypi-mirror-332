# qfactory

A Qt based widget for representing a factory (factories.Factory) instance. This widget
allows for the adding/removing of paths from the factory. Equally it allows for plugins
to be enabled/disabled.

## Install

```
pip install qfactory
```

## Example

This example demonstrates how the widget works and how it updates based on the changes
within the factory.

```python
import qtility
from factories.examples import zoo
from qfactory import FactoryWidget

# -- Instance the example which comes with the factories module
zoo_instance = zoo.Zoo()

# -- Now instance a QApplication and then our Factory widget. We pass
# -- the factory as an argument to the widget. The widget will bind into
# -- the factory signals and represent that factory
qapp = qtility.app.get()

w = FactoryWidget(factory=zoo_instance.factory)
w.show()

qapp.exec()
```
