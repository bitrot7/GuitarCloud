from bottle import redirect
from .base import BaseController


class DashboardController(BaseController):

    def __init__(self):
        super(DashboardController, self).__init__()
        return

    def mydashboard(self):

        if super(DashboardController, self).check_login(super(DashboardController, self).get_username(),
                                                        super(DashboardController, self).get_password()):
            return '''
                <form action="/dashboard" method="post">
                    <input type="file" name="pic" accept="audio/*">
                    <input type="submit">
                </form>
                 '''
        print("name = " + self.get_username())
        return redirect('/login')

    def do_music(self):
        return "<p>processing..</p>"
