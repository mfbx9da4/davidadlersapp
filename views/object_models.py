import os.path as path 
from os.path import dirname

import webapp2
import jinja2
from google.appengine.ext import db

template_dir = path.join(dirname(dirname(__file__)), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

def blog_key(name='default'):
    return db.key.from_path('blogs', name)


class BlogPost(db.Model):
    """Models an individual Guestbook entry with an author, content, and date."""
    subject = db.StringProperty(multiline=False, required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str('blog-post.html', p=self)

    def toDict(post):
        dic = dict()
        dic['subject'] = post.subject
        dic['content'] = post.content
        dic['created'] = post.created.strftime("%b %d, %Y")
        dic['last_modified'] = post.last_modified.strftime("%b %d, %Y")
        return dic


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def error(self, string, *args, **kwargs):
        webapp2.logging.error(string, *args, **kwargs)