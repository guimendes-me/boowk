from db import database

class UserModel(database.Model):
    __tablename__ = 'tb_user'

    user_id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(30))
    password = database.Column(database.String(50))
    firstname = database.Column(database.String(20))
    lastname = database.Column(database.String(20))

    idx_username = database.Index('idx_username', username)

    def __init__(self, username, password, firstname, lastname):  
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname

    def json(self):
        return {
            'user_id': self.user_id,
            'username': self.username,            
            'firstname' : self.firstname,
            'lastname' : self.lastname,
        }

    @classmethod
    def find(cls, username):
        user = cls.query.filter_by(username = username).first()
        if user:
            return user
        return None
    
    def save(self):
        database.session.add(self)
        database.session.commit()

    def update(self, username, pasword, firstname, lastname):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname

    def delete(self):
        database.session.delete(self)
        database.session.commit()