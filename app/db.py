from flask_sqlalchemy import SQLAlchemy
import sqlite3

database = SQLAlchemy()


class Database(object):
    
    connectstring: str
    connection: str
    def __init__(self, rdbms):
        self.rdbms = rdbms

    def getconfig(self):
        if self.rdbms == 'SQLITE' or self.rdbms == '':
            self.connectstring = 'sqlite:///boowk.db'
        return self.connectstring

    def connect(self):
        if self.rdbms == 'SQLITE' or self.rdbms == '':
            self.connection = sqlite3.connect('boowk.db')
        return self.connection