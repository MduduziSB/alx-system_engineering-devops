#!/usr/bin/python3
"""
This script  queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints titles of 10 first hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "My-User-Agent"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data.get("data").get("children"):
            print(post["data"]["title"])
    else:
        print("None")
