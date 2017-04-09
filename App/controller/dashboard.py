from bottle import redirect
from .base import BaseController


class DashboardController(BaseController):

    def __init__(self):
        super(DashboardController, self).__init__()
        return

    def mydashboard(self):

        if super(DashboardController, self).check_login(super(DashboardController, self).get_username(),
                                                        super(DashboardController, self).get_password()):
            return '<p>welcome to my dashboard</p>'
        print("name = " + self.get_username())
        return redirect('/login')

