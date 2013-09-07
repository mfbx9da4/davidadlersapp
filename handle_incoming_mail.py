import logging

from google.appengine.api import mail
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

from views.object_models import BaseHandler


class LogSenderHandler(InboundMailHandler):
    def receive(self, mail_message):
        bodies = mail_message.bodies('text/plain')
        for body in bodies:
            logging.info(body[1].decode())

        
        logging.info("--------------------------------")
        mail.send_mail(sender="Davidadlersapp Support <da@davidadlersapp.appspotmail.com>",
                      to="David Adler <dalberto.adler@gmail.com>",
                      subject=mail_message.subject,
                      body=body[1].decode())

class ContactHandler(BaseHandler):
    def post(self):
        email = self.request.get('email')
        name = self.request.get('name')
        subject = self.request.get('subject')
        msg = self.request.get('message')
        if email and msg:
          msg = 'Name : ' + name + ', email : ' + email + ' sent you the following: \n' + self.request.get('message')
          mail.send_mail(sender="Davidadlersapp Support <da@davidadlersapp.appspotmail.com>",
                        to="David Adler <dalberto.adler@gmail.com>",
                        subject=subject,
                        body=msg)
          self.render('thankyou.html')
        else:
          self.render('error.html', error_message="Please enter an email address and message!")