import bottle
import os
from bottle import run
from controller.login import LoginController
from controller.dashboard import DashboardController
from controller.default import DefaultController


def login_routing(login_controller):
    bottle.route('/login', 'GET', login_controller.login)
    bottle.route('/login', 'POST', login_controller.do_login)
    bottle.route('/fail', 'GET', login_controller.failed_logon)
    return


def dashboard_routing(dashboard_controller):
    bottle.route('/dashboard', 'GET', dashboard_controller.mydashboard)


def default_route(default_controller):
    bottle.route('/', 'GET', default_controller.index)


def main():
    login_controller = LoginController()
    dashboard_controller = DashboardController()
    default_controller = DefaultController()
    login_routing(login_controller)
    dashboard_routing(dashboard_controller)
    default_route(default_controller)
    run(host='localhost', port='8000')
    return


main()
