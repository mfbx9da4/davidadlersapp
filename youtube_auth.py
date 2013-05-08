from udacity.blog.object_models import BaseHandler
from session import SessionHandler
from webob import Request


# '/yt_handler'
class YtPage(BaseHandler, SessionHandler):
    def get(self):
        if self.request.get('error') == 'access_denied':
            self.session['error'] = 'access_denied'
            return self.redirect( self.session.get('link'))
        else:
            http = Request.blank('/o/oauth2/token')
            http.method = 'POST'
            http.headers['Content-Type'] = 'application/x-www-urlencoded'
            http.host = 'accounts.google.com' 
            #http.path = '/o/oauth2/token'
            
            code = 'code=' + self.request.get('code')
            client_id = '&client_id=788984753858.apps.googleusercontent.com'
            redirect_uri = '&redirect_uri=://davidadlersapp.appspot.com/viewnewsfeed'
            client_secret = '&client_secret=my-super-secret-key'
            grant_type = '&grant_type=autorization_code' 
            body = code + client_id + redirect_uri + client_secret + grant_type
            http.body = body.encode('ascii', 'ignore')            

            return self.redirect(uri='accounts.google.com/o/oauth2/token', request=http)

    def post(self):
        self.response.write("ok")

# '/yt_auth'
class YtAuthPage(BaseHandler):
        def get(self):
            #redirect( flow.step1_get_authorize_url() )
            #credentials = flow.step2_exchange(code)
            auth_url = 'https://accounts.google.com/o/oauth2/auth?'
            client_id = '&client_id=788984753858.apps.googleusercontent.com'
            redirect_uri = '&redirect_uri=https://davidadlersapp.appspot.com/yt_handler'
            scope = '&scope=https://www.googleapis.com/auth/youtube'
            response_type = '&response_type=code'
            access_type = '&access_type=offline'
            return self.redirect(auth_url + client_id + redirect_uri + scope + response_type + access_type)
            #flow = OAuth2WebServerFlow(client_id = client_id1, client_secret='your_client_secret',scope=scope1,redirect_uri=redirect_uri)
            #redirect( flow.step1_get_authorize_url() )
            # credentials = flow.step2_exchange(code)



