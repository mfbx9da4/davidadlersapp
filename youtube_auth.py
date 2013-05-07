from udacity.blog.object_models import BaseHandler
from session import SessionHandler
from oauth2client.client import OAuth2WebServerFlow

# '/yt_handler'
class YtPage(BaseHandler, SessionHandler):
	def get(self):
		if self.request.get('error') == 'access_denied':
 			self.session['error'] = 'access_denied'
		else:
            flow = OAuth2WebServerFlow(client_id = client_id,
                           client_secret='your_client_secret',
                           scope=scope1,
                           redirect_uri=redirect_uri)
            self.session['credentials'] = flow.step2_exchange(self.request.get('code'))

 	def post(self):
		self.response.write("ok")

# '/yt_auth'
class YtAuthPage(BaseHandler):
     	def get(self):
            redirect( flow.step1_get_authorize_url() )
            # credentials = flow.step2_exchange(code)
            #auth_url = 'https://accounts.google.com/o/oauth2/auth?'
            client_id1 = '788984753858.apps.googleusercontent.com'
            redirect_uri = 'http://davidadlersapp.appspot.com/yt_handler'
            scope1 = 'http://www.googleapis.com/auth/youtube'
            #response_type = '&response_type=code'
            #access_type = '&access_type=offline'
         	#return self.redirect(auth_url + client_id + redirect_uri + scope + response_type + access_type)
            flow = OAuth2WebServerFlow(client_id = client_id1,
                           client_secret='your_client_secret',
                           scope=scope1,
                           redirect_uri=redirect_uri)
            redirect( flow.step1_get_authorize_url() )
            # credentials = flow.step2_exchange(code)



