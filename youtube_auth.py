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
            auth_url = 'https://accounts.google.com/o/oauth2/auth?'
            client_id = 'client_id=788984753858.apps.googleusercontent.com'
            redirect_uri = '&redirect_uri=http://davidadlersapp.appspot.com/yt_handler'
            scope = '&scope=http://www.googleapis.com/auth/youtube'
            response_type = '&response_type=code'
            access_type = '&access_type=offline'
         	return self.redirect(auth_url + client_id + redirect_uri + scope + response_type + access_type)



