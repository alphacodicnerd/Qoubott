#################
#AUTHOR - Tanya Srivastava
#Github - alphacodicnerd
#instagram - mydialectblog
#twitter - quobot
#################



import tweepy
from time import sleep


consumer_key = 'your consumer key'
consumer_secret = 'your consumer secret key'
access_token = 'your access token'
access_token_secret = 'your access secret token'
# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

for tweet in tweepy.Cursor(api.search, q=('#hashtag1 OR #hashtag2 OR #hashtag3'), lang='en',result_type='popular').items(100): #replace hashtags to your desired hashtags
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)
        id = tweet.id #prints the id of the tweet
        status = api.get_status(id)
        print(status)
        count = status.retweet_count
        if(count>100): #gets tweet whose retweet count is greater than > 100
            # Retweet tweets if retweet count>100
            print("Retweet count:",count)
            tweet.retweet()
            print('Retweeted the tweet')
        else:
            print("Can't retweet with count :",count)
        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

