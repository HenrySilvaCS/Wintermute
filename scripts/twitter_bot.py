import tweepy as tp
import time

consumer_key =
consumer_secret = 
acess_token = 
acess_secret = 


auth = tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(acess_token,acess_secret)
api = tp.API(auth)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}\n'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('TIMER ENDED\n\n\n\n\n')


class OPERATE:

    def __init__(self,path_to_tweets):

        self.path = path_to_tweets


    def read_tweets(self):

        with open(self.path, 'r', errors='replace', encoding='utf-8') as f:
            self.tweets = f.readlines()
        return self.tweets

    def authenticate(self,consumer_key,consumer_secret,acess_token,acess_secret):

        self.ck_auth = consumer_key
        self.cs_auth = consumer_secret
        self.at_auth = acess_token
        self.as_auth = acess_secret
        self.auth = tp.OAuthHandler(self.ck_auth,self.cs_auth)
        self.auth.set_access_token(self.at_auth,self.as_auth)
        self.api = tp.API(self.auth)

    def tweet(self):
        list_tweets = list(self.tweets)
        for i in range(len(list_tweets)):
            status = list_tweets[i]
            self.api.update_status(status=status)
            with open("tweets.txt",'a') as f:
                f.write("#30082020:" + list_tweets[i])
            countdown(14400)


#####
OPERATE = OPERATE("tweets_to_post.txt")
OPERATE.read_tweets()
OPERATE.authenticate(consumer_key,consumer_secret,acess_token,acess_secret)
OPERATE.tweet()


