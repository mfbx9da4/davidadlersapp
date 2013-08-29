from newsfeed import NewsFeed

token = 'AAAEFtAQcXSMBACZCqVzIXjIeN0IAGbJ0ffSj5wPydFBD5jexYAEbbptSZCexxZCwszlKcjpDmWzbeNwlKUC4OKw45IEI5qfRZAeB1yBewAZDZD'

nf = NewsFeed(token)
print '<br>'.join(nf.getNewsFeedVideos())
nf.getNewsFeedVideosPage(3)
