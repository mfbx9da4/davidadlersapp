"""The form elements where the user inputs their username, 
password, password again, and email address must be named 
"username", "password", "verify", and "email", respectively. The form
method must be POST, not GET. Upon invalid user input, your web
app should re-render the form for the user. Upon valid user input
, your web app should redirect to a welcome page for the user. You must enter the full
url into the supplied textbox above, including the path. For example, our example app is
running at http://udacity-cs253.appspot.com/unit2/signup, but if we instead only entered 
http://udacity-cs253.appspot.com/
then the grading script would not work.

Username: "^[a-zA-Z0-9_-]{3,20}$" Password: "^.{3,20}$" Email: "^[\S]+@[\S]+\.[\S]+$"
Example code for validating a username is as follows:

  import re
  USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
  def valid_username(username):
    return USER_RE.match(username)

"""

import os
import random
import string
import hashlib

import webapp2
import jinja2
from google.appengine.ext import db


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

from validate_form import valid_email, valid_pwd, valid_username, valid_verify


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)



def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))


def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return h, salt


def valid_pw(name, pw, h):
    return make_pw_hash(name, pw, h[-5:]) == h



class User(db.Model):
    username = db.StringProperty(required=True)
    pwd_hash = db.StringProperty(required=True)
    salt = db.StringProperty()


class SignupHandler(BaseHandler):
    def get(self):
        self.render('blog-signup.html')

    def post(self):
        form_is_valid = self.validForm()
        if not (self.userExists()) and form_is_valid:
                self.registerUser()
                self.redirect('/blog/welcome')
        else:
            self.render('blog-signup.html', **self.form)

    def registerUser(self):
        h, salt = make_pw_hash(self.form['uname'], self.form['pwd'])
        u = User(username=self.form['uname'], pwd_hash=h, salt=salt)
        u.put()
        self.response.set_cookie('user_id', '%s|%s' % (u.key().id(), h))


    def userExists(self):
        self.q = User.all().filter('username =', self.form['uname'])
        if self.q.get():
            self.form['uname_error'] = 'user exists'
            return True

    def validForm(self):
        self.form = {}
        self.form['uname'] = self.request.get('username')
        self.form['uname_error'] = valid_username(self.form['uname'])
        self.form['pwd'] = self.request.get('password')
        self.form['pwd_error'] = valid_pwd(self.form['pwd'])
        self.form['verify'] = self.request.get('verify')
        self.form['verify_error'] = valid_verify(self.form['verify'], self.form['pwd'], self.form['pwd_error'])
        self.form['email'] = self.request.get('email')
        self.form['email_error'] = valid_email(self.form['email'])
        return self.noErrors()

    def noErrors(self):
        if '' == self.form['pwd_error'] == self.form['verify_error'] == self.form['uname_error']:
            return True


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        cookie = self.request.cookies.get('user_id')
        if cookie:
            user_id, h = cookie.split('|')
        else:
            return self.redirect('/blog/signup')
        user = User.get_by_id(int(user_id))
        if user:
            if user.pwd_hash == h:
                self.response.out.write("Welcome, " + user.username)
            else:
                return self.redirect('/blog/signup')
        else:
            return self.redirect('/blog/signup')


    def validCookie(self):
        browser_h = self.request.cookies.get('user_id')
        h, salt = make_pw_hash(self.form['uname'], self.form['pwd'], self.q.get().salt)
        if h == browser_h:
            return True

class LoginHandler(BaseHandler):
    def get(self):
        self.render('blog-login.html')

    def post(self):
        self.validForm()
        self.passwordsMatching()
        # if self.validForm() and self.passwordsMatching():
        #     self.redirect('/welcome')

    def validForm(self):
        self.form = {}
        self.form['uname'] = self.request.get('username')
        self.form['uname_error'] = valid_username(self.form['uname'])
        self.form['pwd'] = self.request.get('password')
        self.form['pwd_error'] = valid_pwd(self.form['pwd'])
        return self.noErrors()

    def noErrors(self):
        if '' == self.form['pwd_error'] == self.form['uname_error']:
            return True

    def passwordsMatching(self):
        q = User.all()
        q.filter('username = ', self.form['uname'])
        user = q.fetch(1)
        if user:
            user = user[0]
            pw_hash, s = make_pw_hash(user.username, self.form['pwd'], user.salt)
            if pw_hash == user.pwd_hash:
                self.response.set_cookie('user_id', '%s|%s' % (user.key().id(), pw_hash))
                self.redirect('/blog/welcome')
            else:
                self.write('Wrong username or password')
        else:
            self.write('User not found')
        # self.render('loggedIn.html', users=user)

class LogoutHandler(BaseHandler):
    def get(self):
        self.response.set_cookie('user_id', '')
        self.redirect('/blog/signup')

