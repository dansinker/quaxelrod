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


class GoodsPage(webapp.RequestHandler):
  
  def Render(self, template_file, template_values = {}):
     path = os.path.join(os.path.dirname(__file__), 'templates', template_file)
     self.response.out.write(template.render(path, template_values))
  
  def get(self):
    self.Render("goods.html",)



class MainPage(webapp.RequestHandler):
  
  def Render(self, template_file, template_values = {}):
     path = os.path.join(os.path.dirname(__file__), 'templates', template_file)
     self.response.out.write(template.render(path, template_values))
  
  def get(self):
    self.Render("index_ajax.html",)

application = webapp.WSGIApplication([
  ('/', MainPage), 
  ('/g', GoodsPage), 
  ],debug=False)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
  
