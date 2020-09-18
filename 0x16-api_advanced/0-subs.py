#!/usr/bin/python3
"""Module that queries the Reddit API, sets a custom User-Agent
and ensures not following redirects."""
import requests


def number_of_subscribers(subreddit):
    """Send GET request. Arg: <string> with given subreddit
       Return: <int> No. Subscribers or 0 if subreddit is invalid"""
    base_url = 'https://www.reddit.com/r/'
    url = "{}{}/about.json".format(base_url, subreddit)
    headers = {'user-agent': 'holbie1626'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
