import bottle

from bottle import run
from controller.login import LoginController


#entry

def routing(controller):
    bottle.route('/login', 'GET', controller.login)
    bottle.route('/login', 'POST', controller.do_login)
    return

def main():
    controller = LoginController()
    routing(controller)
    run(host='localhost',port='8080')
    return

main()
