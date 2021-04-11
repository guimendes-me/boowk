from db import database
from sqlalchemy.ext.indexable import index_property
from cryptography.fernet import Fernet


class CredentialModel(database.Model):
    __tablename__ = 'tb_credential'

    id_credential = database.Column(database.Integer, primary_key='True')
    fk_username = database.Column(database.String(36), database.ForeignKey('tb_user.username'), index=True)
    ev_link = database.Column(database.String(200), nullable=True)
    ev_email = database.Column(database.String(200), nullable=True)
    ev_password = database.Column(database.String(200), nullable=True)

    idx_fk_username = database.Index('idx_fk_username', fk_username)

    def __init__(self, fk_username, ev_link, ev_email, ev_password):       
          
        key = b'VnTrZV2i3UfH-VHxKfvXL1NP7gOZyoqBvB0KbQ5sZZ4='
        cipher_suite = Fernet(key)        
        ev_email = bytes(ev_email, 'utf-8')
        ev_password = bytes(ev_password, 'utf-8')
        self.ev_link = ev_link
        self.fk_username = fk_username
        self.ev_email = cipher_suite.encrypt(ev_email)
        self.ev_password = cipher_suite.encrypt(ev_password)
               

    def json(self):
        return {
            'id_credential': self.id_credential,
            'username': self.fk_username,            
            'ev_email' : self.ev_email,
            'ev_password' : self.ev_password
        }

    @classmethod
    def find(cls, fk_username):
        user = cls.query.filter_by(fk_username = fk_username).first()
        if user:
            return user
        return None
    
    def save(self):
        database.session.add(self)
        database.session.commit()

    def update(self, fk_username, ev_email, ev_password):
        self.fk_username = fk_username
        self.ev_email = ev_email
        self.ev_password = ev_password        

    def delete(self):
        database.session.delete(self)
        database.session.commit()