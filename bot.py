
import tweepy
import requests
import time

def get_tweet():
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': API_NINJA_KEY})
    if response.status_code == requests.codes.ok:
        tweet = response.json()
    else:
        print("Error:", response.status_code, response.text)
    return tweet[0]


####### API KEYS ###############
API_NINJA_KEY = "1RQFDtiwVntITI47GFBI1A==Cm1SDRqnqro6uOUI"
API_KEY = 'MB9LwGLpk7wqDNMZxcHOVzz24'
API_SECRET_KEY = 'xuCdIVeC5Xv2S1fPGGeWGdWctiXsTDrs5DXOyo8OT1oE20ZFau'
ACCESS_TOKEN = '1511031536870727684-unszK3cKvNhwKDVxL5aTiQHrzudiVg'
ACCESS_TOKEN_SECRET = '4LcNqZdbd2e2aG052FXtOBTHBZtoAjVT8pV4Rm7q9PTBw'

#Authenticate twtter api
authenticator = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
authenticator.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(authenticator)

#Gets user
user = api.get_user(screen_name="JacobsBot2")

tweet = get_tweet()




tweet = get_tweet()
tweet = tweet["fact"]

go = True
while(go):
    tweet = get_tweet()
    tweet = tweet["fact"]
    api.update_status(tweet)
    time.sleep(3600)
    
##Prints the recent followers of my account J__anderson13
"""
for follower in user.followers():
    print(f"{follower.name} follows {user.name}")
"""