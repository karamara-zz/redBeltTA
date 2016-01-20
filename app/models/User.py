from system.core.model import Model
import re
from flask import Flask
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt=Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
class User(Model):
	def __init__(self):
		super(User, self).__init__()
	def create(self, user):
		errors = []
		query_fetch="select * from users where email= '{}' limit 1".format(user['email'])
		if self.db.query_db(query_fetch):
			errors.append("Your Email already exist")
		if len(user['name']) < 2 :
			errors.append("Your name should be longer than 2 characters")
		if not user['DOB']:
			errors.append("You must put date of birth")
		if len(user['password']) < 8 :
			errors.append("Your password should be longer than 8 characters")
		if len(user['email']) < 2 :
			errors.append("Your email should be longer than 2 characters")
		if not EMAIL_REGEX.match(user['email']):
			errors.append("The email you entered {} is not a valid email address!".format(user['email']))
		if errors:
			return{"status":False, 'errors':errors}
		pw_hash=bcrypt.generate_password_hash(user['password'])
		query="insert into users (name,dateOfBirth,email,password,created_at,updated_at) values ('{}','{}','{}','{}',now(),now())".format(user['name'],user['DOB'],user['email'],pw_hash)
		self.db.query_db(query)
		user=self.db.query_db(query_fetch)[0]
		return {"status":True, 'user':user}
	def loginVal(self,login):
		errors=[]
		query_fetch="select * from users where email = '{}' limit 1".format(login['email'])
		query_fetch=self.db.query_db(query_fetch)
		if not query_fetch:
			errors.append("Your information doesn't exist in our database")
		if not errors:
			if bcrypt.check_password_hash(query_fetch[0]['password'],login['password']):
				return {'status':True, 'user':query_fetch[0]}
		errors.append("Your information doesn't match in our database")
		return{'status':False, 'errors':errors}