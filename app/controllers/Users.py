from system.core.controller import *
from datetime import datetime
class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model("User")
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        if session:
            return redirect('/appointments')
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        return self.load_view('login.html')
    def register(self):
        print "resister kicks in "
        if not request.form['password'] == request.form['cfPassword']:
            flash("your password doesn't match")
            return redirect('/')
        else:
            user_info  = {
            'name':request.form['name'],
            'email':request.form['email'],
            'password':request.form['password'],
            'DOB': request.form['DOB']
            }
        status = self.models['User'].create(user_info)
        if status['status'] == True:
            flash("Created the account successfully, log in please")
            return redirect('/')
        else:
            for error in status['errors']:
                flash(error)
            return redirect('/')
    def logout(self):
        session.clear()
        return redirect('/')
    def login(self):
        print "loging in"
        login_info = {
            'email' : request.form['email'],
            'password' : request.form['password']
        }
        status = self.models['User'].loginVal(login_info)
        if status['status'] == True:
            print status
            session['name'] = status['user']['name']
            session['id'] = status['user']['id']
            session['current'] = datetime.now()
            print session
            return redirect('/appointments')
        else:
            for error in status['errors']:
                flash(error)
            return redirect('/')