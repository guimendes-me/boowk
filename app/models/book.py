from db import database, Database
from .book_author import BookAuthorModel
from .author import AuthorModel
import uuid

class BookModel(database.Model):

    #book_author = BooksAuthorsModel()

    def generate_uuid(self):
        return str(uuid.uuid1())

    __tablename__ = 'tb_book'
    #id_book = database.Column(database.Integer, primary_key=True)
    id_book = database.Column(database.String(36), primary_key=True, default=generate_uuid)
    #book_uuid = database.Column(database.String(36), primary_key=True, default=generate_uuid)
    title = database.Column(database.String(100))
    subtitle = database.Column(database.String(100))
    booktype = database.Column(database.String(10))
    #authors = database.relationship('AuthorModel', secondary=book_author.ass_book_author, backref=database.backref('tb_authors', lazy='dynamic'))
    authors = database.relationship('AuthorModel', secondary="ass_book_author")
    edtions = database.relationship('EdtionModel', cascade="all, delete") #recebe a lista de objetos edições
    

    def __init__(self, title, subtitle, booktype):          
        self.title = title
        self.subtitle = subtitle
        self.booktype = booktype        
        

    def json(self):
        return {
            'id_book': self.id_book,
            'title': self.title,            
            'subtitle' : self.subtitle,
            'booktype' : self.booktype,
            'authors': [author.json() for author in self.authors],
            'edtions': [edtion.json() for edtion in self.edtions]
        }

    @classmethod
    def find(cls, key, field='title', like=True):        
        #book = cls.query.filter_by(id_book = id_book).first()
        
        if field=='title' and like==True:
            book = cls.query.filter(BookModel.title.like(f'%{key}%')).first()
        if field=='id_book':
            book = cls.query.filter_by(id_book=key).first()
        if book:
            return book
        return None
        
    
    def save(self):           
        database.session.add(self)
        database.session.commit()

    def update(self, title, author):
        self.id_book = id_book
        self.title = title
        self.subtitle = subtitle
        self.booktype = booktype

    def delete(self):
        database.session.delete(self)
        database.session.commit()
        return {"mensage": "Book not found"}            