import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
	if not USER_RE.match(username):
		return 'invalid uname'
	else:
		return ''

PWD_RE = re.compile(r"^.{3,20}$")
def valid_pwd(pwd):
	if not PWD_RE.match(pwd):
		return 'invlaid pwd'
	else:
		return ''

def valid_verify(verify, pwd, pwd_err):
	if not pwd_err:
		if not verify == pwd:
			return 'not matching pwds'
		else: 
			return ''
	else: 
		return ''

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
	if email:
		if not EMAIL_RE.match(email):
			return 'invalid email'
		else:
			return ''