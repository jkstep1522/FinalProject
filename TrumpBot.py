# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
# argfile = str(sys.argv[1])
 
CONSUMER_KEY = 'rl0WBM4z8nzbylwtFn6bCDaLG'
CONSUMER_SECRET = '0TZPx8jm4rNdJmJPGd2brOMAOWcCzmZK9MkHYuAp4Haou4Wxbf'
ACCESS_KEY = '936011008145018880-r3XFmCPdf8bJuHQp7qmzKRM4tm6C2GC'
ACCESS_SECRET = 'AvKo8waEVeyIJw8AZrRVWgITq5OtURkO4YFY8CnJhReq9'
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
