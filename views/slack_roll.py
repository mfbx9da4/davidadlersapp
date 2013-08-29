import webapp2
from udacity.blog.object_models import BaseHandler
import math

class RollHandler(BaseHandler):
    def get(self):
        return self.render('roll.html')

    def post(self):
        d = float(self.request.get('d'))
        w = float(self.request.get('w'))
        s = float(self.request.get('s'))
        layers = int(s / w)
        length = 0
        for n in range(layers):
            length +=  math.pi * (( 2 * w ** n) + d) 

        return self.write(length)



