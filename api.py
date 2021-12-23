import tweepy
from twython import Twython

# # KEY ASHRIL

# # ACCESS TOKEN ASHRIL


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
