# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
# argfile = str(sys.argv[1])
 
CONSUMER_KEY = 'TestKeyrl0WBM4z8nzbylwtF'
CONSUMER_SECRET = 'TestSecret0TZPx8jm4rN'
ACCESS_KEY = 'TestAccess9360110081450188'
ACCESS_SECRET = 'TestSecretAvKo8waEVeyIJ'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

argfile = 'HelloWorld.txt'
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes
