import json
import urllib2
from random import *
from termcolor import *
from datetime import datetime

if __name__ == '__main__':
  
  token = 'AAAEFtAQcXSMBAFZC0WpcVyWrqbFPqgo2HZCvmuCV6kmjQoqhJBFCzQrc0RBrIlDTNrZB7iWrnH3Tp774c4cusVY7P5ZAb4o8HpS1u4dOlQZDZD'
  s = urllib2.urlopen('https://graph.facebook.com/me/home?access_token='+token)
  
  jo = json.loads(s.read())
  random_story = choice(jo['data'])
  #random_story = jo['data'][0]
  print
  for key, value in jo['data'][-1].iteritems():
    st = key,':', value
    print colored(st,'white','on_red', attrs=['bold'])
  
  print 
  print random_story['type'], 'from', random_story['from']['name'], 
  try : x = random_story['message']; del x; print 'saying:\n', colored(random_story['message'],'green')
  except KeyError: print colored('without message','yellow')
  
