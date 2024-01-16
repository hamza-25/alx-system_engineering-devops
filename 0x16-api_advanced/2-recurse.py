#!/usr/bin/python3
"""Query, returns the number hot titles"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Recursive function, returns hot titles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "hamzaApp/1.0 by hamza-25"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for count_title in results.get("children"):
        hot_list.append(count_title.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
