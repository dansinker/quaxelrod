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
    reply_to_username= db.StringListProperty()
    reply_to_tweet_id= db.StringProperty()
    date = db.StringProperty()
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
    attendee = simplejson.loads(json)
    a = Attendee(
        name=attendee['name'],
        bio=attendee['bio'],
        photo=attendee['photo'],
        company=attendee['company'],
        company_url=attendee['company_url'],
        hometown=attendee['hometown'],
        links=attendee['links'],
        registrant_type=attendee['registrant_type'],
        badge_type=attendee['badge_type'],
        user_id=attendee['user_id'], 
        user_url=attendee['user_url'],
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
  
