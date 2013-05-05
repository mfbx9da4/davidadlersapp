"""
export PATH=$PATH:/home/david/Dropbox/Programming/Python/Miscellaneous/extensions/google_appengine
dev_appserver.py helloworld/
appcfg.py update helloworld/

"""

__website__ = 'http://davidadlersapp.appspot.com/'


import os
import re

import webapp2
import jinja2

from udacity.ROT13.main import RotHandler, PreviousEntries
from udacity.signup.main import SignupHandler, ThanksHandler
from udacity.blog.main import BlogPage, EntryPage, PermalinkPage, EditPage
from udacity.blog.object_models import BaseHandler
from fb_yt import ViewNewsFeed, fb
from gae.GAE_tutorial import MainPage, Guestbook, Channel
from youtube_auth import YtPage 
from youtube_auth import YtAuthPage 

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)



class Home(BaseHandler):
      def get(self): 
            pages = stripOutRouteStrings(app.router.match_routes)
            self.render('home.html', pages=pages)

def stripOutRouteStrings(routes):
      strs = []
      for r in routes:
            strs.append(re.findall('/[a-zA-Z/0-9.]*', r.template)[0])
      return strs

class Wiki(BaseHandler):
      def get(self): 
            self.render('wiki.html')

class GDev(BaseHandler):
      def get(self): 
            self.render('gdev2.html')
    
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

app = webapp2.WSGIApplication([('/', Home),
                               ('/gae', MainPage),
                               ('/sign', Guestbook),
                               ('/wiki', Wiki),
                               ('/gdev', GDev),
                               ('/welcome', ThanksHandler),
                               ('/channel.html', Channel),
                               ('/viewnewsfeed', ViewNewsFeed),
                               ('/udacity/blog/newpost', EntryPage),
                               (r'/udacity/blog/(\d+)', PermalinkPage),
                               (r'/udacity/blog/edit/(\d+)', EditPage),
                               ('/udacity/blog', BlogPage),
                               ('/yt_handler', YtPage),
                               ('/yt_auth', YtAuthPage),
                               ('/udacity/blog/', BlogPage),
                               ('/udacity/blog/', BlogPage),
                               ('/udacity/rot13', RotHandler),
                               ('/udacity/signup', SignupHandler),
                               ('/udacity/rot13/entries', PreviousEntries),
                               ('/fb',fb)],
                              debug=True, 
 				config=config)
