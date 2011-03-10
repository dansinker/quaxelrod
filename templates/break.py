import urllib, mechanize
import time
import simplejson
import os
import sys
from multiprocessing import Pool
import pickle


f = open("goods.html","r").read()
tweets_html =  f.split('</li>')
i =1 
tweets = []
for t in tweets_html:
  try:
    try:
      username,tweet_id =t.split('<li class="hentry status main-entry" id="')[1].split('">')[0].split('-')
    except:
      username,tweet_id =t.split('<li class="hentry status in-response-to" id="')[1].split('">')[0].split('-')
  except:
    username = ''
    tweet_id = ''
  try:
    tweet =t.split('<span class="entry-content">')[1].split('</span>')[0]
  except:
    tweet = ''
  try:
    url =t.split('<a class="entry-date" rel="bookmark" href="')[1].split('">')[0]
  except:
    url = ''
  try:
    date =t.split('<span class="published timestamp">')[1].split('</span>')[0]
  except:
    date = ''
  try:
    via =t.split('<span>via ')[1].split('</span>')[0]
  except:
    via = ''
  try:
    reply_to_username, reply_to_tweet_id =t.split('\n    \n  <a href="#')[1].split('">')[0].split('-')
  except:
    reply_to_username= ''
    reply_to_tweet_id = ''

  tweet = {
      'tweet_id':tweet_id,
      'username':username,
      'tweet':tweet,
      'url':url,
      'date':date,
      'via':via,
      'reply_to_tweet_id':reply_to_tweet_id,
      'reply_to_username':reply_to_username,
      }
  tweets.append(tweet)
  print tweet
  i +=1
  print i

f = open("tweets.json","w").write(simplejson.dumps(tweets))


