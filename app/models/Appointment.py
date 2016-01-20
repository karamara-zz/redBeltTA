from system.core.model import Model
from datetime import datetime
class Appointment(Model):
	def __init__(self):
		super(Appointment, self).__init__()
	def index(self, id):
		query = "select * from appointments where user_id = {} order by time desc".format(id)
		return self.db.query_db(query)

	def create(self, appInfo):
		print appInfo
		query="insert into appointments (tasks, status, time, user_id, created_at, updated_at, date) values ('{}', '{}', '{} {}', '{}', now(), now(),{})".format(appInfo['tasks'], "Pending",appInfo['date'], appInfo['time'], appInfo['user_id'], appInfo['date'])
		print query
		self.db.query_db(query)
	def delete(self, id):
		query ='delete from appointments where id = {}'.format(id)
		print query
		self.db.query_db(query)
	def appById(self, id):
		query = "select * from appointments where id = {} limit 1".format(id)
		return self.db.query_db(query)
	def update(self, updateInfo):
		query = 'update appointments set tasks="{}", updated_at = now(), status = "{}", time = "{} {}" where id = {}'.format(updateInfo['tasks'], updateInfo['status'],updateInfo['date'], updateInfo['time'], updateInfo['id'])
		self.db.query_db(query)
	def appVal(self,info):
		errors = []
		print datetime.now(), info['date'], "sdfsdfdsfdaadfasdfsdf"
		if len(info['tasks']) < 2 :
			errors.append("Your tasks should be longer than 2 characters")
		if not info['date']:
			errors.append("You must put date ")
		if not info['time']:
			errors.append("You must put time ")
		if info['date'] < datetime.now().strftime('%Y-%m-%d'):
			errors.append("you can't make appointment that is past")
		if errors:
			print errors
			return{"status":False, 'errors':errors}
		return {"status":True, 'info':info}

