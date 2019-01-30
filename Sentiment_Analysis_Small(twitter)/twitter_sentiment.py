import tweepy
from textblob import TextBlob
import twitter_credential

# Authenticate with twitter API
auth = tweepy.OAuthHandler(twitter_credential.Consumer_key, twitter_credential.Consumer_secret_key)
auth.set_access_token(twitter_credential.Access_token, twitter_credential.Access_token_secret)

# main variable from we will do every thing
api = tweepy.API(auth)

# word for search
search_tweet = api.search('Arup Das')

for tweet in search_tweet:
    print(tweet.text)  # Print only the texts
    # now for sentiment analysis
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

