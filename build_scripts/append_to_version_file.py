#!/usr/bin/env python
from sys import argv
from os import path, remove

current_path = path.dirname(path.realpath(__file__))
version_file_path = path.join(current_path, "compile_version_string.txt")

def get_version_string():
    with open(version_file_path, "r") as file:
        contents = file.readline()
        return contents.strip('"')    

def set_version_string(new_version_string):
    remove(version_file_path)
    with open(version_file_path, "w") as file:
        file.write("\"" + new_version_string + "\"")

if __name__ == "__main__":
    current_version = get_version_string()
    new_version = current_version + "-" + argv[1]
    set_version_string(new_version)