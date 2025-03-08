import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='qfactory',
    version='1.0.1',
    author='Mike Malinowski',
    author_email='mike.external@outlook.com',
    description='A Qt based ui widget to manage a factories.Factory',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>3.1.1',
    url='https://github.com/mikemalinowski/factories',
    packages=setuptools.find_packages(),
    install_requires=[
        "qt.py", "factories",
    ],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
