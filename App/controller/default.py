from bottle import redirect


class DefaultController:
    def __init__(self):
        return

    def index(self):
        return redirect('/login')
