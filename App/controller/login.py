# noinspection PyUnresolvedReferences
import bottle
from bottle import request
from controller.base import BaseController
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
            return "<p>Your login information was correct.</p>"
        else:
            return "<p>Login failed.</p>"

