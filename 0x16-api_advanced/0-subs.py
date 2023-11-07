#!/usr/bin/python3
"""This script queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "My-User-Agent"
    }

    response = requests.get(url,
                            headers=headers,
                            allow_redirects=False)

    if response.status_code < 300:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return (subscribers)
    return (0)
