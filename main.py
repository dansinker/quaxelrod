import os
import hashlib
import base64
import urllib
import logging
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import xmpp_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import urlfetch
from google.appengine.ext import search 
from django.utils import simplejson 
from google.appengine.api import memcache



class Tweet(search.SearchableModel):
    username = db.StringProperty(required=True)
    tweet_id = db.StringProperty()
    via= db.StringProperty()
    url = db.LinkProperty()
    tweet = db.StringProperty()
    reply_to_username= db.StringProperty()
    reply_to_tweet_id= db.StringProperty()
    date_string = db.StringProperty()
    date = db.DateTimeProperty()
    json_dump= db.TextProperty()

    @classmethod
    def SearchableProperties(cls):
        return ['username', 'reply_to_username','tweet']
    
# The web app interface
class MainPage(webapp.RequestHandler):
  
  def Render(self, template_file, template_values = {}):
     path = os.path.join(os.path.dirname(__file__), 'templates', template_file)
     self.response.out.write(template.render(path, template_values))
  
  def get(self):
    self.Render("index_ajax.html",{})

class LoadPage(webapp.RequestHandler):
  
  def post(self):
    json = self.request.body
    print "---"
    print json
    tweet = simplejson.loads(json)
    a = Tweet(
        username=tweet['username'],
        via=tweet['via'],
        tweet=tweet['tweet'].replace('\n',''),
        reply_to_tweet_id=tweet['reply_to_tweet_id'],
        reply_to_username=tweet['reply_to_username'],
        tweet_id=tweet['tweet_id'],
        date_string=tweet['date'],
        json_dump = json,
        )
    a.save()
    self.response.out.write('asd')


application = webapp.WSGIApplication([
  ('/', MainPage), 
  ('/load', LoadPage), 
  ],debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
  
