
from bottle import request, redirect

from .base import BaseController


class LoginController(BaseController):

    def __init__(self):
        super().__init__()
        return

    def login(self):
        return '''
            <form action="/login" method="post">
                Username: <input name="username" type="text" />
                Password: <input name="password" type="password" />
                <input value="Login" type="submit" />
            </form>
        '''

    def do_login(self):
        username = request.forms.get('username')
        password = request.forms.get('password')
        if super(LoginController, self).check_login(username, password):
            redirect_url = self.getlogon_success_url()
            return redirect(redirect_url)
        else:
            redirect_url = self.getlogon_failure_url()
            return redirect(redirect_url)

    def failed_logon(self):
        return '<p> your logon attempt was unsuccessful</p>'

    def getlogon_failure_url(self):
        return '/fail'

    def getlogon_success_url(self):
        return '/dashboard'
