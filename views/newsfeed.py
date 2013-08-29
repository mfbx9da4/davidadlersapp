import json
import urllib2
from random import *
from datetime import datetime
import re

#token = 'AAAEFtAQcXSMBAFZC0WpcVyWrqbFPqgo2HZCvmuCV6kmjQoqhJBFCzQrc0RBrIlDTNrZB7iWrnH3Tp774c4cusVY7P5ZAb4o8HpS1u4dOlQZDZD'


class NewsFeed (object):
    def __init__(self, token):
        self.s = urllib2.urlopen('https://graph.facebook.com/me/home?access_token='+token)
        self.jo = json.loads(self.s.read())
    
    def getNewsFeedString(self):
        return self.s.read()
        
    def getNewsFeedJsonObject(self):
        jo = json.loads(self.s.read())
        return jo
    
    def getNewsFeedVideos(self):
        vid_list = []
        for story in self.jo['data']:
            for k, v in story.iteritems():
                if k == 'link':
                    if re.findall('youtube', v) == ['youtube']:
                        vid_list.append(story[k])
        return vid_list
     
    def getNewsFeedVideosPage(self, depth):
        if depth == 0:
            return []
        vid_list = self.getNewsFeedVideos()
        self.s = urllib2.urlopen(self.jo['paging']['next'])
        self.jo = json.loads(self.s.read())
        vid_list.extend(self.getNewsFeedVideosPage(depth-1))
        #print vid_list
        return vid_list
