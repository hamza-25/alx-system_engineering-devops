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
    users = requests.get(f'{url}users').json()
    todos = requests.get(f'{url}todos').json()
    new_list = []
    new_dict = {}
    all_dict = {}
    for user in users:
        for todo in todos:
            if todo['userId'] == user['id']:
                new_dict['username'] = user['username']
                new_dict['task'] = todo['title']
                new_dict['completed'] = todo['completed']
                new_list.append(new_dict)
                all_dict[user['id']] = new_list
                new_dict = {}
        new_list = []
    with open('todo_all_employees.json', 'w') as js_file:
        json.dump(all_dict, js_file)
