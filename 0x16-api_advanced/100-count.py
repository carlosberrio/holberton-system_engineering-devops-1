#!/usr/bin/python3
"""Recursive function that queries the Reddit API and prints the count
of the frequency of specific words in the titles of all hot articles
for a given subreddit"""
import requests


def count_words(subreddit, word_list, allposts=[], after=""):
    """Prints a sorted count of given keywords
    (<word_list>: case-insensitive, delimited by spaces)"""
    base_url = 'https://www.reddit.com/r/'
    url = "{}{}.json?after={}".format(base_url, subreddit, after)
    headers = {'user-agent': 'holbie1626_t100'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()
    after = data.get('data').get('after')
    posts = data.get('data').get('children')

    if posts:
        allposts += [post.get('data').get('title') for post in posts]

    if after:
        return allposts + count_words(subreddit, word_list, allposts, after="")
    else:
        word_count = {key.lower(): 0 for key in word_list}
        for title in allposts:
            for word in title.split():
                if word.lower() in word_count.keys():
                    word_count[word.lower()] += 1
        dict_to_print = {k: v for k, v in word_count.items() if v > 0}
        keys_sorted = sorted(list(dict_to_print.keys()))
        # Sort dictionary according sorted list(alphabetically) ----:
        for key in sorted(keys_sorted, reverse=True,
                          key=lambda k: dict_to_print[k]):
            print('{}: {}'.format(key, dict_to_print[key]))
        return allposts
