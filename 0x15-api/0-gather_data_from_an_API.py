#!/usr/bin/python3
"""
Module that uses the 'https://jsonplaceholder.typicode.com/' REST API and
given employee ID, returns information about his/her ToDo list progress.
"""
import requests
import sys

if __name__ == "__main__":
    uid = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/users/'
    resp_user = requests.get('{}{}'.format(base_url, uid))
    resp_todos = requests.get('{}{}/todos'.format(base_url, uid))

    if resp_user.status_code != 200:
        raise Exception(
            "Error: {} {}".format(resp_user.status_code, resp_user.reason)
        )
    if resp_todos.status_code != 200:
        raise Exception(
            "Error: {} {}".format(resp_user.status_code, resp_user.reason)
        )
    user = resp_user.json().get('name')
    user_todos = resp_todos.json()
    completed = [todo for todo in user_todos if todo.get('completed')]

    print("Employee {} is done with tasks({}/{}):".format(
            user, len(completed), len(user_todos)))
    for todo in completed:
        print('\t{}'.format(todo.get('title')))
