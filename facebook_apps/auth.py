from rauth.service import OAuth2Service
import re
import webbrowser
from urllib2 import *
# Get a real consumer key & secret from:
# https://developers.facebook.com/apps

website = 'http://davidadlersapp.appspot.com/'
fbid = '287745697930531'
fbsecr = '244b438e67524756fcdaedb24a54e8c5'
newssfeedurl = 'https://graph.facebook.com/me/home?access_token='

facebook = OAuth2Service(
    name='facebook',
    authorize_url='https://graph.facebook.com/oauth/authorize',
    access_token_url='https://graph.facebook.com/oauth/access_token',
    consumer_key=fbid,
    consumer_secret=fbsecr)

redirect_uri = 'https://www.facebook.com/connect/login_success.html'
authorize_url = facebook.get_authorize_url(redirect_uri=redirect_uri,
                                           scope='read_stream',
                                           response_type='token')

print 'Visit this URL in your browser: \n' + authorize_url
#webbrowser.open(authorize_url); 

raw_input()
url_with_code = urlopen(authorize_url).geturl();
#url_with_code = raw_input("Copy URL from your browser's address bar: ")
print url_with_code
#access_token = re.search('#access_token=([^&]*)', url_with_code).group(1)

user = facebook.get('https://graph.facebook.com/me',
                    params=dict(access_token=access_token)).content

print 'currently logged in as: ' + user['link']
