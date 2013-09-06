"""
export PATH=$PATH:/home/david/Dropbox/Programming/Python/Miscellaneous/extensions/google_appengine
dev_appserver.py helloworld/
appcfg.py update helloworld/

"""

__website__ = 'http://davidadlersapp.appspot.com/'


import re

import webapp2
from views.object_models import BaseHandler
from views import blog, signup


class Home(BaseHandler):
    def get(self): 
        self.render('home.html')

def stripOutRouteStrings(routes):
    strs = []
    for r in routes:
        strs.append(re.findall('/[a-zA-Z/0-9._()]*', r.template)[0])
    return strs

class ComingSoon(BaseHandler):
    def get(self): 
        self.render('coming_soon.html')

class ANGN(BaseHandler):
    def get(self): 
        self.render('angn.html')

class Rhythmludus(BaseHandler):
    def get(self): 
        self.render('rhythmludus.html')


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

routes = [('/', Home), ('/imperial', ComingSoon),
        ('/gdocs', ComingSoon), ('/angn', ANGN), ('/pe', ComingSoon),
        ('/slackline', ComingSoon), ('/neuroscience', ComingSoon),
        ('/rhythmludus', Rhythmludus)] + blog_routes


app = webapp2.WSGIApplication(routes,
                              debug=True, 
                              config=config)


