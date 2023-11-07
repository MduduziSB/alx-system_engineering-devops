#!/usr/bin/python3
"""
queries the Reddit API, parses the title of all hot article,
and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
    """
    if word_count is None:
        word_count = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}

    params = {'limit': 100}
    if after:
        params['after'] = after

    sub_info = requests.get(url,
                            params=params,
                            headers=headers,
                            allow_redirects=False)

    if sub_info.status_code != 200:
        return

    info = sub_info.json()

    hot_posts = info.get('data', {}).get('children', [])
    if not hot_posts:
        return

    word_list = list(map(str.lower, word_list))

    for post in hot_posts:
        title = post.get('data', {}).get('title', '').lower()
        words_in_title = title.split()

        for keyword in word_list:
            word_count[keyword] = word_count.get(keyword, 0)\
                    + words_in_title.count(keyword)

    if not info.get("data").get("after"):
        sorted_word_count = sorted(word_count.items(),
                                   key=lambda x: (-x[1], x[0]))

        # Print the sorted results
        for word, count in sorted_word_count:
            if count > 0:
                print("{}: {}".format(word, count))
    else:
        return count_words(subreddit,
                           word_list,
                           word_count,
                           info.get("data").get("after"))
