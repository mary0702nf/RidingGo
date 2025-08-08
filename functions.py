import json

def read_info(filename):
    with open(filename, "r") as file:
        return json.load(file)

def save_info(filename, dict):
    with open(filename, "w") as file:
        json.dump(dict, file)