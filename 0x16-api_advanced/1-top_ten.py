#!/usr/bin/python3
"""define module print 10 title"""
import requests


def top_ten(subreddit):
    """print title"""
    if subreddit is None or type(subreddit) is not str:
        return (0)
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'hamzaApp/1.0 by hamza-25'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    data = response.json().get('data')
    i = 0
    for title in data.get('children'):
        if i == 0:
            i += 1
            continue
        print(title.get('data').get('title'))
        i += 1
