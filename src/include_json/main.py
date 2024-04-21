import json
from include_json.lib import say_hello
import pkg_resources 

def read_json():
    filepath = pkg_resources.resource_filename('include_json','data.json')
    with open(filepath) as file:
        data = json.load(file)

    say_hello()
    print(data)
    return data

if __name__ == "__main__":
    read_json()
    
