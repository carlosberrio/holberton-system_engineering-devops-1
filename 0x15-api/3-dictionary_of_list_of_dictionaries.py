#!/usr/bin/python3
"""
Module that uses the 'https://jsonplaceholder.typicode.com/' REST API
and returns information about all users ToDo list progress
and saves it in a JSON file.
"""
import json
import requests

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'
    resp_all_users = requests.get('{}users/'.format(base_url))
    if resp_all_users.status_code != 200:
        raise Exception(
            "Error: {} {}".format(resp_all_users.status_code,
                                  resp_all_users.reason)
        )
    all_users = resp_all_users.json()

    resp_all_todos = requests.get('{}todos/'.format(base_url))
    if resp_all_todos.status_code != 200:
        raise Exception(
            "Error: {} {}".format(resp_all_todos.status_code,
                                  resp_all_todos.reason)
        )
    todos = resp_all_todos.json()

    json_data = {}
    for user in all_users:
        json_data[user.get('id')] = [
                {
                    "username": user.get('username'),
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                } for todo in todos if todo.get('userId') == user.get('id')
            ]

    with open('todo_all_employees.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile)
