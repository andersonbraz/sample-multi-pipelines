import json


def get_json_to_list(fullpath: str) -> list:
    with open(fullpath, 'r') as file:
        data_list = json.load(file)
    return data_list

