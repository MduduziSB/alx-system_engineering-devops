#!/usr/bin/python3
"""This script exports data in the json format"""

import json
import requests
import sys


if __name__ == "__main__":

    user_url = requests.get("https://jsonplaceholder.typicode.com/users")
    user_url = user_url.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todo_dic = {}

    for idx in user_url:
        task_list = []
        for task in todos:
            if task.get('userId') == idx.get('id'):
                json_data = {
                             "username": idx.get('username'),
                             "task": task['title'],
                             "completed": task['completed']}
                task_list.append(json_data)
        todo_dic[idx.get('id')] = task_list

    filename = "todo_all_employees.json"
    with open(filename, mode='w') as File:
        json.dump(todo_dic, File)
