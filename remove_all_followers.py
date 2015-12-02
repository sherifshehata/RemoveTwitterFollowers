import tweepy

__author__ = 'dedunumax'

'''

This script will remove all the followers from your twitter account. For that first it will block user one by one and
then unblock them. If you are following your followers, you won't be subscribed to them anymore once you run this job.
Rub this script carefully.

Install tweepy using pip. To install tweepy run below command in your terminal.
sudo pip install tweepy

Please replace consumer_key and consumer_secret. Visit https://apps.twitter.com to get your consumer_key and
consumer_secret.

Once you generate consumer key create an access token from same twitter page. Replace access_token and
access_token_secret with provided values. Then run the script.
'''

consumer_key = '<consumer_key>'
consumer_secret = '<consumer_secret>'
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
