import tweepy

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

consumer_key = '<API_Key>'
consumer_secret = '<API_secret>'
access_token = '<access_token>'
access_token_secret = '<access_token_secret>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

followers_list = api.followers_ids(api.me())

for user in followers_list:
    api.create_block(user)
    api.destroy_block(user)
    print user
