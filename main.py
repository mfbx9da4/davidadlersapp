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
from facebook_apps.fb_yt import fb
from facebook_apps.fb_yt import ViewNewsFeed
from GAE_tutorial import MainPage, Guestbook, Channel

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

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
                               ('/udacity/blog/', BlogPage),
                               ('/udacity/rot13', RotHandler),
                               ('/udacity/signup', SignupHandler),
                               ('/udacity/rot13/entries', PreviousEntries),
                               ('/fb',fb)],
                              debug=True)
