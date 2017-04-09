
import pymysql


class BaseController(object):

    username = ''
    password = ''

    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='default',
            db='test'
        )
        return

    def getcredentials(self, username, password):
        cursor = self.connection.cursor()
        command = "SELECT * FROM user WHERE name=%s AND password=%s"
        cursor.execute(command, (username, password))
        return cursor.fetchone()

    def check_login(self, username, password):
        row = self.getcredentials(username, password)
        if row:
            BaseController.username = row[1]
            BaseController.password = row[2]
            return True
        BaseController.username = ''
        BaseController.password = ''
        return False

    def get_username(self):
        return BaseController.username

    def get_password(self):
        return BaseController.password
