import os
import webapp2
import jinja2
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from newsfeed import NewsFeed


fbid = '287745697930531'
fbsecr = '244b438e67524756fcdaedb24a54e8c5'


class fb(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('fb.html')
        self.response.out.write(template.render())


class ViewNewsFeed(webapp2.RequestHandler):
    def post(self):
        token = self.request.get('q')
        nf = NewsFeed(token)
        vid_list = nf.getNewsFeedVideosPage(20)
        html = ''
        for x in vid_list:
            a = '<iframe id="ytplayer" type="text/html" width="640" height="360" src="%s" frameborder="0" allowfullscreen><br>' % x
            html += a
        self.response.write(html)
    
    def get(self):
        a = '<iframe id="ytplayer" type="text/html" width="640" height="360" src="https://www.youtube.com/embed/Zhawgd0REhA" frameborder="0" allowfullscreen>'
        self.response.write(a)


