from db import database
import uuid



class AuthorModel(database.Model):

    def generate_uuid():
        return str(uuid.uuid1())

    __tablename__ = 'tb_author'

    #id = database.Column(database.Integer, primary_key=True)
    id_author = database.Column(database.String(36), primary_key=True, default=generate_uuid)
    firstname = database.Column(database.String(20))
    middlename = database.Column(database.String(20))
    lastname = database.Column(database.String(20))    


    def __init__(self, firstname, middlename, lastname):  
        self.firstname  = firstname
        self.middlename = middlename
        self.lastname   = lastname

    def json(self):
        return {
                'id_author': self.id_author,
                'firstname': self.firstname,
                'middlename': self.middlename,
                'lastname': self.lastname,                                
        }

    @classmethod
    def find(cls, key, field='firstname', like=True):        
        #author = cls.query.filter_by(id_author = id_author).first()
        
        if field=='firstname' and like==True:
            author = cls.query.filter(AuthorModel.firstname.like(f'%{key}%')).first()
        if field=='id_author':
            author = cls.query.filter_by(id_author=key).first()
        if author:
            return author
        return None
        
    
    def save(self):
        database.session.add(self)
        database.session.commit()

    def update(self, firstname, middlename, lastname):
        self.firstname  = firstname
        self.middlename = middlename
        self.lastname   = lastname

    def delete(self):
        database.session.delete(self)
        database.session.commit()        