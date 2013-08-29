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




class Nav(BaseHandler):
    def get(self): 
        pages = stripOutRouteStrings(app.router.match_routes)
        self.render('home.html', pages=pages)

class Me(BaseHandler):
    def get(self): 
        self.render('about_me.html')

def stripOutRouteStrings(routes):
    strs = []
    for r in routes:
        strs.append(re.findall('/[a-zA-Z/0-9._()]*', r.template)[0])
    return strs

class Imperial(BaseHandler):
    def get(self): 
        self.render('coming_soon.html')

class GDocs(BaseHandler):
    def get(self): 
        self.render('coming_soon.html')

class ANGN(BaseHandler):
    def get(self): 
        self.render('coming_soon.html')

class PE(BaseHandler):
    def get(self): 
        self.render('coming_soon.html')

class Rhythmludus(BaseHandler):
    def get(self): 
        self.render('coming_soon.html')

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

routes = [('/nav', Nav), ('/me', Me), ('/imperial', Imperial),
        ('/gdocs', GDocs), ('/angn', ANGN), ('/pe', PE),
        ('/rhythmludus', Rhythmludus)] + blog_routes

# ('/yt_handler', YtPage),
# ('/yt_auth', YtAuthPage),
# ('/slack_roll', RollHandler ),
# ('/udacity/signup', SignupHandler),
# ('/udacity/login', LoginHandler),
# ('/udacity/logout', LogoutHandler),
# ('/udacity/rot13/entries', PreviousEntries),
# ('/fb',fb)

app = webapp2.WSGIApplication(routes,
                              debug=True, 
                              config=config)


