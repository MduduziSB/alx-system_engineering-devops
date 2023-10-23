#!/usr/bin/python3
"""This script exports data in the CSV format"""

import csv
import json
import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{user_url}/users/{employee_id}")
    name = user_response.json().get("username")
    tasks_response = requests.get(f"{user_url}/todos?userId={employee_id}")
    tasks_data = tasks_response.json()

    # Export data to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL, lineterminator='\n')

        for task in tasks_data:
            csv_writer.writerow([employee_id,
                                name, task["completed"], task["title"]])
