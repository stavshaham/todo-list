# file_handler.py - by Stav Shaham
# This file handles all related functions to the files.

import json

# This function saves the new data in the json file
def save_data(data):
    """
    This function saves the data into a json file
    :param data:
    :type data: List
    :return:
    """
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# This function reads the data
def load_data():
    """
    This function loads the data from the json file
    :return data: returns the data from the json file
    """
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data