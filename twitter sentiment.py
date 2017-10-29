
#twiter sentimental analysis 
import tweepy
import re
from tweepy import OAuthHandler
#from tweepy import stream
from textblob import TextBlob
import json

#providing key and secret
consumer_key = "eykkod7OEjixMXjikeh2IsWg6"
consumer_secret = "OGySoD7OOHyfJQxnLgB95MbPAc2WYXDIdcccuoahoMfZvqViOP"

#providing token and token secret 
access_token = "768439398681677824-TPtIY7r23LshRgc5lYM1yXXi9YdHoBk"
access_token_secret = "9rPas7cfKH2UCvRXiohXPXV9Z8YSHAyeme46A1NS3ArDO"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#api variable to perform operations for twitter
api = tweepy.API(auth)

#printing json twwet per line
def process_or_store(tweet):
    print(json.dumps(tweet))
#storing tweets in json
#process_or_store is a placeholder for our custom implementation
for status in tweepy.Cursor(api.home_timeline).items(20):
    #process a single status
    process_or_store(status._json)

    
#for List of all followers
for friend in tweepy.Cursor(api.friends).items(20):
    process_or_store(friend._json)
    
#list of all our tweets
for tweet in tweepy.Cursor(api.user_timeline).items(20):
    process_or_store(tweet._json)

'''
#empty tweets list
tweets=[]
#file which we want to open in second arguement
save_file = open('out.json','a')


class CustomStreamListener(tweepy.StreamListener):
    def _init_(self,api):
        self.api = api
        super(tweepy.StreamListener, self)._init_()
        
        self.save_file = tweets
        
    def on_data(self, tweets):
        self.save_file.append(json.loads(tweet))
        print(tweet)
        save_file.write(str(tweet))
        
''' 
        
'''        
public_tweets = api.search('Cricket')

for tweets in public_tweets:
    print(tweets.text)
    analysis = TextBlob(tweets.text)
    print(analysis.sentiment)
    #print('Polarity of above :',analysis.sentiment.polarity)
    
'''

 
