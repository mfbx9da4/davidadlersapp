from facebook_apps.newsfeed import NewsFeed
from udacity.blog.object_models import BaseHandler

fbid = '287745697930531'
fbsecr = '244b438e67524756fcdaedb24a54e8c5'


class fb(BaseHandler):
    def get(self):
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


