#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information about
ARGS:
    fisrt arg: is the id of the employee
"""
import csv
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
                username = user['username']
        completed = 0
        total_task = 0
        title_completed_task = []
        all_tasks = []
        response_todo = response_todo.json()
        for do in response_todo:
            if do['userId'] == int(sys.argv[1]):
                if do['completed'] is True:
                    title_completed_task.append(do['title'])
                    completed += 1
                all_tasks.append(do['title'])
                total_task += 1
        matrix_rows = []
        for title in all_tasks:
            if title in title_completed_task:
                matrix_rows.append([sys.argv[1], username, "True", title])
            else:
                matrix_rows.append([sys.argv[1], username, "False", title])
        with open(f'{sys.argv[1]}.csv', "w") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerows(matrix_rows)
