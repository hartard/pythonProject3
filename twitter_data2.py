# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:06:10 2020

@author: Falco
"""

# importing necessary modules
import tweepy as tw
import pandas as pd

# access keys of twitter api
consumer_key = 'ckey'
consumer_secret = 'cskey'
access_token = 'atoken'
access_token_secret = 'astoken'

# authentification
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# defining search
search_words = '#Ischgl2'
date_since = '2020-11-01'

# collecting tweets
tweets = tw.Cursor(api.search,
                   q=search_words,
                   lang='de',
                   since=date_since).items(20)

# printing tweet text
for tweet in tweets:
    print(tweet.text)

new_search = search_words + " -filter:retweets"

tweets = tw.Cursor(api.search,
                   q=new_search,
                   lang='de',
                   since=date_since).items(20)

users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]

print(users_locs)

tweet_text = pd.DataFrame(data=users_locs,
                          columns=['user', 'location'])

print(tweet_text)
