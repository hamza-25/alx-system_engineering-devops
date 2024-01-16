#!/usr/bin/python3
"""define module total subs"""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return (0)
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'hamzaApp/1.0 by hamza-25'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return (0)
    response_json = response.json()
    return (response_json['data']['subscribers'])
