# Project

This project demonstrates how to package and read from a JSON file in Python.

## Project Structure

```
project/
├── src/
│   ├── project/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── data.json
├── unittests/
│   ├── __init__.py
│   └── test_main.py
├── setup.py
└── README.md
```

In the `setup.py` file, the package structure is defined to include the `src` folder and the `data.json` file.

## Reading JSON File

The `main.py` file in the `src` folder reads the `data.json` file using `pkg_resources` and `json` modules.

```python
import pkg_resources
import json

def read_json():
    json_file = pkg_resources.resource_filename('project','data.json')

    with open(json_file) as file:
        data = json.load(file)

    print(data)
    return data

if __name__ == "__main__":
    read_json()
```

## Unit Testing

Unit tests for the `read_json` function are written in the `test_main.py` file in the `unittests` folder.

```python
import unittest
from project.main import read_json

class TestMain(unittest.TestCase):
    def test_read_json(self):
        data = read_json()
        self.assertEqual(data["name"], "John Doe")
        self.assertEqual(data["age"], 30)
        self.assertEqual(data["city"], "New York")

if __name__ == "__main__":
    unittest.main()
```

## Building the Project

To build the project, run `python setup.py bdist_wheel`. Make sure to run `pip install wheel` before building the project.

## Running Unit Tests

To run the unit tests, use `pip install -e .` in the root directory to make the package available for testing.

This project showcases how to package and read from a JSON file in Python, along with writing unit tests for the functionality.

# Python Packaging Guide

This guide covers two important concepts in Python packaging: `package_dir` and `find_packages()`. Understanding these concepts will help you create a package that can be easily installed and imported in a Python environment.

## package_dir

The `package_dir` option in the `setup()` function is used to define a directory layout that is different from the Python's default one. By default, Python assumes that your packages (directories containing `__init__.py` files) are located directly under the directory where your `setup.py` script resides.

The `package_dir` option takes a dictionary where the keys are package names and the values are directory names relative to your `setup.py` script.

For example, if you have a package named `my_package` in a directory called `src`, your `package_dir` would look like this:

```python
package_dir={'': 'src'}
```

This tells Python that the packages are under the `src` directory instead of being directly under the directory where `setup.py` is located.

## find_packages()

The `find_packages()` function is used to automatically discover and list all packages in your project. A package is defined as a directory that contains an `__init__.py` file.

By default, `find_packages()` assumes that your packages are located directly under the directory where your `setup.py` script resides. But if your packages are in a different directory, you can specify that directory using the `where` parameter.

For example, if your packages are under the `src` directory, you would call `find_packages()` like this:

```python
find_packages(where='src')
```

This tells `find_packages()` to look for packages under the `src` directory instead of the default directory.

## Example

Here is an example of a `setup.py` script that uses `package_dir` and `find_packages()`:

```python
from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    description='A sample Python package',
    author='Your Name',
    author_email='your.email@example.com',
    url='http://example.com',
    license='MIT',
    packages=find_packages(where='src'),
    include_package_data=True,
    package_dir={'': 'src'},
    package_data={
        "": ["*.json"]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points={
        'console_scripts': ['my_package=my_package.main:main']
    },
    keywords='sample package',
    python_requires=">=3.6",
    setup_requires=['wheel'],
)
```

After defining your `setup.py` script, you can install your package using pip:

```sh
pip install -e .
```

And then import it in your Python code:

```python
import my_package
```

It's important to remember that `__init__.py` files should not be empty. If you want to import the package directly, you should import something in `__init__.py` or define something inside `__init__.py`.
