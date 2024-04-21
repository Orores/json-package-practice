# Project

This is a Python project that demonstrates how to package and read from a JSON file.

Import ant things to consider

Project structure:

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


setup.py
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"project": ["*.json"]},

When the src folder is sleected then the hierarrchy inside the src folder is used for the project

package_data make the any .json include too

the jsoon can htne be used in main if packg_tools are used:

import pkg_resources
import json
import os

def read_json():
    json_file = pkg_resources.resource_filename('project','data.json')

    with open(json_file) as file:
        data = json.load(file)

    print(data)
    return data

if __name__ == "__main__":
    read_json()

don't fprget that a return ins necessary for unittests.

Unittestinging:

the unittest don't work if you run them just like
python unittest -discover -s tests, because it can'T find the paraent package.

in order to run the unittest you need to run pip install -e . in the directory where the srup.py is (in this cas eroot directory.) This will make the package available fto the unitest


import unittest
from project.main import read_json

class TestMain(unittest.TestCase):
    def test_read_json(self):
        data = read_json()
        print('My data: ',data)
        print(type(data))
        self.assertEqual(data["name"], "John Doe")
        self.assertEqual(data["age"], 30)
        self.assertEqual(data["city"], "New York")

if __name__ == "__main__":
    unittest.main()



Building the project
The prohect is build with python setup.py bdist_wheel
for that pip install wheel needs to be run.

When importing stuff like lets say there is a lib in the project folder where main is the main shall import lib like for .lib import some_function
