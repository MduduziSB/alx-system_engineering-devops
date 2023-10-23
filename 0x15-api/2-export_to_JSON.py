#!/usr/bin/python3
"""This script exports data in the json format"""

import json
import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{user_url}/users/{employee_id}")
    name = user_response.json().get("name")
    tasks_response = requests.get(f"{user_url}/todos?userId={employee_id}")
    tasks_data = tasks_response.text
    tasks = json.loads(tasks_data)

    dic = {}
    task_list = []

    for task in tasks:
        json_data = {
                     "task": task['title'],
                     "completed": task['completed'],
                     "username": name}
        task_list.append(json_data)

    dic[employee_id] = task_list

    filename = employee_id + '.json'
    with open(filename, mode='w') as File:
        json.dump(dic, File)
