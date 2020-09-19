#!/usr/bin/python3
"""Module that queries the Reddit API, sets a custom User-Agent
and ensures not following redirects."""
import requests


def top_ten(subreddit):
    """Send GET request. Arg: <string> with given subreddit. Prints the
    titles of the first 10 hot posts, or None if subreddit is invalid"""
    base_url = 'https://www.reddit.com/r/'
    url = "{}{}.json".format(base_url, subreddit)
    headers = {'user-agent': 'holbie1626_t1'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    data = response.json().get('data', {}).get('children', {})
    if response.status_code != 200 or not data:
        print(None)
    for post in data:
        print(post.get('data', {}).get('title'))
