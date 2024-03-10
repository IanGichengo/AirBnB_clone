#!/usr/bin/python3
"""Store first object"""

import json
from models.user import User

class FileStorage:
    """serializes instances to a JSON file and deserializes JSON
    file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file"""
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
                for key, value in self.__objects.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'User':
                        self.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
