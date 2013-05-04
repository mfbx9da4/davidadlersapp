from udacity.blog.object_models import BaseHandler

class YtPage(BaseHandler):
     	def connect(self):
         	self.redirect( 'https://accounts.google.com/o/oauth2/auth?client_id=788984753858.apps.googleusercontent.com&redirect_uri=http://davidadlersapp.appspot.com/yt_auth&scope=https://www.googleapis.com/auth/youtube&response_type=code&access_type=offline')

	def get(self):
		if self.request.get('error') == 'access_denied' :
                 	html = 'error'
			self.response.write(html)
		else:
                 	html = self.request.get('code')
			self.response.write(html)
  			
 	def post(self):
		self.response.write("ok")
 		
