from udacity.blog.object_models import BaseHandler
from session import SessionHandler

class YtPage(BaseHandler, SessionHandler):
	def get(self):
		if self.request.get('error') == 'access_denied' :
 			self.session['error'] = 'access_denied'
			return self.redirect(self.session.get('link'))
		else:
 			self.session['code'] = self.request.get('code')
			return self.redirect(self.session.get('link'))
 	def post(self):
		self.response.write("ok")

class YtAuthPage(BaseHandler):
     	def get(self):
         	return self.redirect( 'https://accounts.google.com/o/oauth2/auth?client_id=788984753858.apps.googleusercontent.com&redirect_uri=http://davidadlersapp.appspot.com/yt_handler&scope=https://www.googleapis.com/auth/youtube&response_type=code&access_type=offline')
 
	 		
