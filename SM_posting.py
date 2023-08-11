
# Project: Automated Social Media Posting

# Description: This project automates the process of posting content to social media platforms, such as Twitter, Facebook, or LinkedIn, at specified times. It allows you to schedule and manage your social media posts in advance, saving time and effort.

import tweepy
import json
import time

def post_to_twitter(api_key, api_secret_key, access_token, access_token_secret, content, posting_time):
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    api.update_status(content)
    print(f"Posted on Twitter: '{content}' at {posting_time}")

if __name__ == "__main__":
    # Read Twitter API credentials from a configuration file
    with open("twitter_credentials.json", "r") as f:
        twitter_credentials = json.load(f)

    content = "Hello, Twitter! This is an automated post using Python."
    posting_time = "2023-08-07 12:00:00"  # Specify the posting time in YYYY-MM-DD HH:mm:ss format

    while True:
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        if current_time >= posting_time:
            post_to_twitter(
                twitter_credentials["api_key"],
                twitter_credentials["api_secret_key"],
                twitter_credentials["access_token"],
                twitter_credentials["access_token_secret"],
                content,
                posting_time
            )
            break

        time.sleep(60)  # Check the current time every minute