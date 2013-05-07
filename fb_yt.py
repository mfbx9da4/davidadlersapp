from facebook_apps.newsfeed import NewsFeed
from udacity.blog.object_models import BaseHandler
from youtube_auth import YtPage
from session import SessionHandler

fbid = '287745697930531'
fbsecr = '244b438e67524756fcdaedb24a54e8c5'


class fb(BaseHandler, SessionHandler):
    def get(self):
        # test if the token 'code' exists, if it doesn't then it ask youtube a
        # a auth token
        if not self.session.get('code'):
            self.session['link'] = 'http://davidadlersapp.appspot.com/fb'
            self.redirect('yt_auth')
	    else:
       	    self.render('fb.html')


class ViewNewsFeed(BaseHandler):
    def post(self):
        token = self.request.get('q')
        nf = NewsFeed(token)
        vid_list = nf.getNewsFeedVideosPage(1)
        self.render('videos.html', videos=vid_list)
    
    def get(self):
        a = '<iframe id="ytplayer" type="text/html" width="640" height="360" src="https://www.youtube.com/embed/Zhawgd0REhA" frameborder="0" allowfullscreen>'
        self.response.write(a)


