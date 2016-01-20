"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from datetime import datetime
class Appointments(Controller):
    def __init__(self, action):
        super(Appointments, self).__init__(action)
        self.load_model("Appointment")
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        if not session:
            return redirect('/')
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """

        session['current'] = datetime.now()
        # print session
        appointments = self.models['Appointment'].index(session['id'])
        # print appointments
        return self.load_view('index.html', appointments = appointments)
    def create(self):
        app_info = {
            'tasks' : request.form['tasks'],
            'date' : request.form['date'],
            'time' : request.form['time'],
            'user_id': session['id']
            }
        # print app_info
        updateVal = self.models['Appointment'].appVal(app_info)
        if updateVal['status'] == True:
            self.models['Appointment'].create(app_info)
        else:
            print "there is error"
            for error in updateVal['errors']:
                flash(error)
        return redirect('/appointments')
    def delete(self, id):
        self.models['Appointment'].delete(id)
        return redirect('/appointments')
    def update(self,id):
        # print "updating the information by id", id
        updateInfo = {
            'id': id,
            'tasks': request.form['tasks'],
            'date' : request.form['date'],
            'time' : request.form['time'],
            'status' : request.form['status']
        }
        # print updateInfo
        updateVal = self.models['Appointment'].appVal(updateInfo)
        if updateVal['status'] == True:
            self.models['Appointment'].update(updateInfo)
        else:
            print "there is error"
            for error in updateVal['errors']:
                flash(error)
        return redirect('/appointments')
    def edit(self, id):
        editApp = self.models['Appointment'].appById(id)[0]
        # print editApp
        appointments = self.models['Appointment'].index(session['id'])
        return self.load_view('index.html', appointments = appointments, editApp = editApp)
