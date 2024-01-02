#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information about
ARGS:
    fisrt arg: is the id of the employee
"""
import requests
import sys

if __name__ == "__main__":
    response_user = requests.get('https://jsonplaceholder.typicode.com/users')
    response_todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    if response_user.status_code == 200 and response_todo.status_code == 200:
        response_user = response_user.json()
        for user in response_user:
            if user['id'] == int(sys.argv[1]):
                emp_name = user['name']
        completed = 0
        total_task = 0
        title_completed_task = []
        response_todo = response_todo.json()
        for do in response_todo:
            if do['userId'] == int(sys.argv[1]):
                if do['completed'] is True:
                    title_completed_task.append(do['title'])
                    completed += 1
                total_task += 1
        print(f'Employee {emp_name} is done '
              f'with tasks({completed}/{total_task}):')
        for title in title_completed_task:
            print(f'\t {title}')
