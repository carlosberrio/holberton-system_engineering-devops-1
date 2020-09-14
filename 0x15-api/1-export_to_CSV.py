#!/usr/bin/python3
"""
Module that uses the 'https://jsonplaceholder.typicode.com/' REST API and
given employee ID, returns information about his/her ToDo list progress
and saves it in a CSV file.
"""
import csv
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
            "Error: {} {}".format(resp_todos.status_code, resp_todos.reason)
        )
    user = resp_user.json().get('username')
    user_todos = resp_todos.json()

    with open('{}.csv'.format(uid), 'w', encoding='utf-8') as csvfile:
        user_csv = [[uid, user, todo.get('completed'), todo.get('title')]
                    for todo in user_todos]
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(user_csv)
