#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information about
"""
import requests
from sys import argv
import json

response_user = requests.get('https://jsonplaceholder.typicode.com/users')
response_todo = requests.get('https://jsonplaceholder.typicode.com/todos')

if response_user.status_code == 200 and response_todo.status_code == 200:
    response_user = response_user.json()
    for user in response_user:
        if user['id'] == int(argv[1]):
            emp_name = user['name']

    completed = 0
    total_task = 0
    title_completed_task = []
    response_todo = response_todo.json()
    for do in response_todo:
        if do['userId'] == int(argv[1]):
            if do['completed'] is True:
                title_completed_task.append(do['title'])
                completed += 1
            total_task += 1

    print(f'Employee {emp_name} is done with tasks({completed}/{total_task}):')
    for title in title_completed_task:
        print(f'\t{title}')
