#!/usr/bin/python3
"""
This script queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    if after:
        url += "&after={}".format(after)

    headers = {
        "User-Agent": "My-User-Agent"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data.get("data", {}).get("children", [])
        if not children:
            return hot_list
        else:
            for post in children:
                hot_list.append(post["data"]["title"])
            return recurse(subreddit, hot_list, data["data"]["after"])
    else:
        return None
