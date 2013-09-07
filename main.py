"""
export PATH=$PATH:/home/david/Dropbox/Programming/Python/Miscellaneous/extensions/google_appengine
dev_appserver.py helloworld/
appcfg.py update helloworld/

"""

__website__ = 'http://davidadlersapp.appspot.com/'


import re

import webapp2
from google.appengine.ext import db

from views.object_models import BaseHandler
from views import blog, signup
from handle_incoming_mail import LogSenderHandler, ContactHandler

class Portfolio(db.Model):
    """Portfolio entry."""
    title = db.StringProperty(multiline=False, required=True)
    url_name = db.StringProperty(multiline=False, required=True)
    html_file_name = db.StringProperty(multiline=False, required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

class Home(BaseHandler):
    def get(self): 
        self.render('home.html')

class Rhythmludus(BaseHandler):
    def get(self): 
        self.render('rhythmludus.html')

class PortfolioHandler(BaseHandler):
    def get(self, url_name):
        query = Portfolio.all().filter('url_name =', url_name)
        p = query.get() 
        if p:
            self.render(p.html_file_name, p=p)
        else:
            self.render('coming_soon.html')

class Admin(BaseHandler):
    def get(self):
        portfolios = Portfolio.all().fetch(1000)
        self.render('admin.html', portfolios=portfolios)

    def post(self):
        title = self.request.get('title')
        url_name = self.request.get('url_name')
        html_file_name = self.request.get('html_file_name')
        p = Portfolio(title=title, url_name=url_name, html_file_name=html_file_name)
        p.put()
        self.get()


config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

blog_routes = [('/blog', blog.BlogPage), ('/blog/newpost', blog.EntryPage),
    (r'/blog/(\d+)',  blog.PermalinkPage),
    (r'/blog/edit/(\d+)', blog.EditPage), 
    ('/blog/signup', signup.SignupHandler),
    ('/blog/login', signup.LoginHandler),
    ('/blog/logout', signup.LogoutHandler),
    ('/blog/welcome', signup.ThanksHandler)]

routes = [('/', Home), ('/admin', Admin), (r'/portfolio/(\w+)', PortfolioHandler),
        ('/mail', ContactHandler), LogSenderHandler.mapping()] + blog_routes


app = webapp2.WSGIApplication(routes,
                              debug=True, 
                              config=config)


