#!/usr/bin/python3
"""define module total subs"""
import requests


# def number_of_subscribers(subreddit):
#     """number of subscribers"""
#     if subreddit is None or type(subreddit) is not str:
#         return (0)
#     url = f'http://www.reddit.com/r/{subreddit}/about.json'
#     headers = {'User-Agent': 'hamzaApp/1.0 by hamza-25'}
#     response = requests.get(url, headers=headers)
#     response_json = response.json()
#     subs = response_json.get("data", {}).get("subscribers", 0)
#     return int(subs)
def number_of_subscribers(subreddit):
    """Function that returns the number of redit subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {
        "User-Agent": "MyRedditBot:v1.0.0"
    }
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 404:
        return 0
    data = response.json().get("data")
    return data.get("subscribers")
