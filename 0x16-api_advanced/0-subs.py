#!/usr/bin/python3
import requests
import sys


def number_of_subscribers(subreddit):
    """number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return (0)
    url = f'https://www.reddit.com/r/{sys.argv[1]}/about.json'
    response = requests.get(url)
    response_json = response.json()
    return (response_json['data']['subscribers'])
