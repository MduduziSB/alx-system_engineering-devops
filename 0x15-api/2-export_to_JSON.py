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

    dic = {str(employee_id): []}

    for task in tasks:
        json_data = {
                     "task": task['title'],
                     "completed": task['completed'],
                     "username": name}

        dic[str(employee_id)].append(json_data)

    encoded_data = json.dumps(dic)
    filename = employee_id + '.json'
    with open(filename, mode='w') as File:
        File.write(encoded_data)
