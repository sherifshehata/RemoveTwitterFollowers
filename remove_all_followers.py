import tweepy
import time
from datetime import datetime

__author__ = 'original dedunumax, fokred and changed by SherifShehata' #forked from https://gist.github.com/dedunumax/91992ac6f1940be5d391

'''
This script will remove all the followers from your twitter account. For that first it will block user one by one and
then unblock them. 

Install tweepy module using pip. To install tweepy run below command in your terminal.
sudo pip install tweepy

Please replace consumer_key and consumer_secret. Visit https://apps.twitter.com to get your consumer_key and
consumer_secret.

Once you generate consumer key create an access token from same twitter page. Replace access_token and
access_token_secret with provided values. Then run the script.
'''

def do_or_wait_15(code):
    #print(code)
    while(True):
        try:
            return eval(code)
        except Exception as e:
            print(e)
                
            print("waiting 15 minutes")
                
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)

            time.sleep(60*15) 

consumer_key = '<API_Key>'
consumer_secret = '<API_secret>'
access_token = '<access_token>'
access_token_secret = '<access_token_secret>'
screen_name = '<user_to_delete_followers>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

followers_list = api.get_follower_ids(screen_name=SCREEN_NAME)

print(len(followers_list))
      
i = 1
for user in followers_list:
    print (i, user)
    
    api.create_block(user_id==user)
    api.destroy_block(user_id==user)
    print user
    
    i = i + 1
