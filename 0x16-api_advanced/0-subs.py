#!/usr/bin/python3
"""define module total subs"""
import requests
import sys


def number_of_subscribers(subreddit):
    """number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return (0)
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url)
    if response.status_code != 200:
        return (0)
    response_json = response.json()
    return (response_json['data']['subscribers'])
