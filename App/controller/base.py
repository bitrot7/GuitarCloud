
import pymysql


class BaseController:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='default',
            db='test'
        )
        return

    def getCredentials(self, username, password):
        cursor = self.connection.cursor()
        command = "SELECT * FROM user WHERE name=%s AND password=%s"
        cursor.execute(command, (username, password))
        return cursor.fetchone()

    def check_login(self, username, password):
        if (self.getCredentials(username, password)):
            return True
        return False