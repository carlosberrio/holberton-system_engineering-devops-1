#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Send GET request.
    Arg: subreddit: <string> with given subreddit.
         hot_list: <list> list that will contain titles of all articles.
         after: <string> pagination value for separating pages of responses.
    Returns:
         List containing the titles of all hot articles for a given subreddit.
         If no results are found for the given subreddit, will return None."""

    base_url = 'https://www.reddit.com/r/'
    url = "{}{}.json?after={}".format(base_url, subreddit, after)
    headers = {'user-agent': 'holbie1626_t2'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()
    after = data.get('data').get('after')
    posts = data.get('data').get('children')
    if posts:
        hot_list.extend(post.get('data').get('title') for post in posts)
    if after:
        return hot_list + recurse(subreddit, hot_list, after)
    else:
        return hot_list
