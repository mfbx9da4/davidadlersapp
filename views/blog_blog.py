"""
In order to be graded correctly for this homework, there are a
few things to keep in mind. We'll be grading your web app
 by POSTing new blog entries to your form and checking that
  they appear on your blog's front page. There
   are a few main issues you need to keep in mind in order for this to work:

We assume your form to create new blog entries is at a path
of '/newpost' from your blog's front page. That is, if your blog's
front page is at 'www.myblog.com/blog', then the
form is at 'www.myblog.com/blog/newpost'.
The form method must be POST, not GET. The form input boxes must have the

names 'subject'
and 'content'

in order for the grading script to correctly post to
them. You must enter the full url into the supplied textbox above,
including the path to your blog's front page. For example, our example
app is running at http://cs253-homework-sean.appspot.com/blog, but if we
instead only entered http://udacity-cs253.appspot.com/ then the grading script 
 would not work. Don't forget to escape your output!
If you're interested in the css styling file we use for the example page, the link is here.
"""
import json

from object_models import BaseHandler, BlogPost

# class JSONpage
# 	def get(self):
# 		query
# 		dict .subj, .cont, .date strfTime
# 		escape "" to JSON
# 		set header to JSON
# 		writeJSON

# class JSONFront



class JSON(BaseHandler):
	def get(self, blog_id):
		post = BlogPost.get_by_id(int(blog_id))
		self.response.headers['Content-Type'] = "application/json"
		if post:
			self.response.out.write(json.dumps(post.toDict()))

class JSONFront(BaseHandler):
	def get(self):
		last10 = BlogPost.all().order('-created').fetch(10)
		dics = []
		for post in last10:
			dics.append(post.toDict())
		self.response.headers['Content-Type'] = "application/json"
		self.response.out.write(json.dumps(dics))


class EntryPage(BaseHandler):
	def get(self):
		self.render('blog-newpost.html')

	def post(self):
		self.getEntry()
		if not self.errors:
			self.putPost()
			self.redirect('/blog/%d' % self.post.key().id())
		else:
			kw = dict(self.entry.items() + self.errors.items())
			self.render('blog-newpost.html', **kw)

	def getEntry(self):
		self.entry = {}
		sub_entry = self.request.get('subject')
		content_entry = self.request.get('content')
		self.entry['subject'] = sub_entry if sub_entry else '' 
		self.entry['content'] = content_entry if content_entry else ''
		self.checkForErrors()

	def putPost(self):
		subj = self.entry['subject'] 
		cont = self.entry['content']
		self.post = BlogPost(subject=subj, content=cont)
		self.post.put()

	def checkForErrors(self):
		self.errors = {}
		if not self.entry['subject']:
			self.errors['subject_error'] = 'No subject'
		if not self.entry['content']:
			self.errors['content_error'] = 'No content'


class BlogPage(BaseHandler):
	def get(self):
		entries_query = BlogPost.all().order('-created')
		self.render('blog-front.html', posts=entries_query.fetch(10))

class PermalinkPage(BaseHandler):
	def get(self, blog_id):
		e = BlogPost.get_by_id(int(blog_id))
		self.render('blog-permalink.html', post=e)

class EditPage(BaseHandler):
	def get(self, blog_id):
		post = BlogPost.get_by_id(int(blog_id))
		self.render('blog-edit.html', post=post)

	def post(self, blog_id):
		post = BlogPost.get_by_id(int(blog_id))
		post.subject = self.request.get('subject')
		post.content = self.request.get('content')
		post.put()
		self.redirect('/blog/%d' % post.key().id())



