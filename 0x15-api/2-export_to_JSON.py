#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information about
ARGS:
    fisrt arg: is the id of the employee
"""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f'{url}users/{sys.argv[1]}').json()
    todos = requests.get(f'{url}todos?userId={sys.argv[1]}').json()
    new_list = []
    new_dict = {}
    for todo in todos:
        new_dict['task'] = todo['title']
        new_dict['completed'] = todo['completed']
        new_dict['username'] = user['username']
        new_list.append(new_dict)
        new_dict = {}
    new_dict = {}
    new_dict[f'{sys.argv[1]}'] = new_list
    with open(f'{sys.argv[1]}.json', 'w') as js_file:
        json.dump(new_dict, js_file)
