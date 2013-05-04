from facebook_apps.newsfeed import NewsFeed
from udacity.blog.object_models import BaseHandler
from youtube_auth import YtPage

fbid = '287745697930531'
fbsecr = '244b438e67524756fcdaedb24a54e8c5'


class fb(BaseHandler):
    def get(self):
       # self.render('fb.html')
       self.redirect( 'https://accounts.google.com/o/oauth2/auth?client_id=788984753858.apps.googleusercontent.com&redirect_uri=http://davidadlersapp.appspot.com/yt_auth&scope=https://www.googleapis.com/auth/youtube&response_type=code&access_type=offline')
     # ytpage = YtPage()
#      ytpage.connect() 


class ViewNewsFeed(BaseHandler):
    def post(self):
        token = self.request.get('q')
        nf = NewsFeed(token)
        vid_list = nf.getNewsFeedVideosPage(1)
        self.render('videos.html', videos=vid_list)
    
    def get(self):
        a = '<iframe id="ytplayer" type="text/html" width="640" height="360" src="https://www.youtube.com/embed/Zhawgd0REhA" frameborder="0" allowfullscreen>'
        self.response.write(a)


