#!/usr/bin/python3
"""script returns information about his/her TODO list progress"""

import json
import requests
import sys


base_url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":

    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{user_url}/users/{employee_id}")
    name = user_response.json().get("name")
    tasks_response = requests.get(f"{user_url}/todos?userId={employee_id}")
    tasks_data = tasks_response.json()

    # Count completed tasks and total tasks
    completed_tasks = [task for task in tasks_data if task["completed"]]
    completed = len(completed_tasks)
    num_tasks = len(tasks_data)

    # Print the output in the required format
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, num_tasks))

    for task in completed_tasks:
        print(f"\t {task['title']}")
