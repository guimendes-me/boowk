from db import database

class UserModel(database.Model):
    __tablename__ = 'users'

    user_id = database.Column(database.Integer, primary_key='True')
    login = database.Column(database.String(30))
    password = database.Column(database.String(50))
    firstname = database.Column(database.String(20))
    lastname = database.Column(database.String(20))


    def __init__(self, login, password, firstname, lastname):  
        self.login = login
        self.password = password
        self.firstname = firstname
        self.lastname = lastname

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login,            
            'firstname' : self.firstname,
            'lastname' : self.lastname,
        }

    @classmethod
    def find(cls, login):
        user = cls.query.filter_by(login = login).first()
        if user:
            return user
        return None
    
    def save(self):
        database.session.add(self)
        database.session.commit()

    def update(self, login, pasword, firstname, lastname):
        self.login = login
        self.password = password
        self.firstname = firstname
        self.lastname = lastname

    def delete(self):
        database.session.delete(self)
        database.session.commit()