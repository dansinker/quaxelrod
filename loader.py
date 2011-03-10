import os, sys, csv
import simplejson
import httplib, urllib
import urllib, urllib2

if __name__ == '__main__':

  api_url = 'http://localhost:8080/load'
  #api_url = 'http://www.isxgoing.com/load'

  tweets = open("./templates/tweets.json", 'r').read()
  tweets = simplejson.loads(tweets)

                   
  for t in tweets:
    f = urllib2.urlopen(api_url, simplejson.dumps(t))
    data = f.read()
    print data
    f.close()
    print "uploaded "+t['tweet_id']


    

