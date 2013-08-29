# from apiclient.discovery import build
from google.appengine.ext import webapp
from oauth2client.appengine import OAuth2Decorator

decorator = OAuth2Decorator(
  client_id='788984753858.apps.googleusercontent.com',
  client_secret='your_client_secret',
  scope='http://www.googleapis.com/auth/youtube')

# service = build('calendar', 'v3')

class AuthHandler(webapp.RequestHandler):

  @decorator.oauth_required
  def get(self):
    # Get the authorized Http object created by the decorator.
    http = decorator.http()
    # Call the service using the authorized Http object.
    request = service.events().list(calendarId='primary')
    response = request.execute(http=http)


