# importing neccessary modules and packages
import pandas as pd
import csv
import re 
import string
import preprocessor as p
import tweepy

consumer_key = 'Rs5p7znGjoEWNC5PmkxwPENC1'
consumer_secret = 'e8tAkkfGaMppRnaUJnCaWmfr9x7zXOmKrG2NkGv3nUYrShUqDB'
access_key= '2490439219-dRwCZyCYAqAWh4nDawtTH4RGCowgdjbTfdHuTvj'
access_secret = 'IZo28USVGCo4HXbvxvOY7BLIGpkuLLHPo6lkiLLdGHyFu'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True)
 
csvFile = open('messages.csv', 'a')
csvWriter = csv.writer(csvFile)
 
search_words = ""      # enter your words

new_search = search_words + " -filter:retweets"

for tweet in tweepy.Cursor(api.search_tweets,q=new_search,count=10,
                           lang="en",
                           since_id=0).items():
    print("extracting")
    csvWriter.writerow([tweet.text.encode('utf-8')])
    msg = tweet.text.encode('utf-8')
    clean_tweet = p.cleaner(msg)

    