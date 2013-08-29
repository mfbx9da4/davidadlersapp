import wsgiref.handlers
import urllib
import cgi
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db

import gdata.youtube
import gdata.youtube.service
import gdata.media
import gdata.geo
import gdata.alt.appengine

class StoredToken(db.Model):
    user_email = db.StringProperty(required=True)
    session_token = db.StringProperty(required=True)

class AuthSub(webapp.RequestHandler):
	def __init__(self):
		self.current_user = None
		self.token = None
		self.feed_url = 'http://gdata.youtube.com/feeds/api/users/default/uploads'
		self.youtube_scope = 'http://gdata.youtube.com'
		self.developer_key = None
		self.client = gdata.youtube.service.YouTubeService()
		gdata.alt.appengine.run_on_appengine(self.client)

	def get(self):
    self.my_app_domain = 'http://' + self.request._environ[[]'HTTP_HOST']
    self.response.out.write("""<html><head><title>
        hello_authsub: AuthSub demo</title>
        <link type="text/css" rel="stylesheet" href="/stylesheets/main.css" />
        """)

    self.current_user = users.GetCurrentUser()
    self.response.out.write('</head><body>')

    # Split URL parameters if found
    for param in self.request.query.split('&'):
      if param.startswith('token'):
        self.token = param.split('=')[[]1]
      elif param.startswith('feed_url'):
        self.feed_url = urllib.unquote_plus(param.split('=')[[]1])

    if self.current_user:
      self.response.out.write('<a href="%s">Sign Out</a><br /><br />' % (
          users.CreateLogoutURL(self.request.uri)))

      if self.LookupToken():
        self.response.out.write('<div id="video_listing">')
        self.FetchFeed()
        self.response.out.write('</div>')

      else:
        # Check if a one-time use token was passed in the URL parameters
        if self.token:
          self.UpgradeAndStoreToken()
          self.redirect('/')
		else:
		  self.response.out.write('<div id="sidebar"> '
			  '<div id="scopes"><h4>Request a token</h4><ul>')
		  self.response.out.write('<li><a href="%s">YouTube API</a></li>' % (
			  self.client.GenerateAuthSubURL(
			  self.my_app_domain, self.youtube_scope, secure=False, session=True))
			  )