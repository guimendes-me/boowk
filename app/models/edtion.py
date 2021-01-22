from db import database
import uuid

class EdtionModel(database.Model):

    def generate_uuid():
        return str(uuid.uuid1())

    __tablename__ = 'tb_edtion'

    #id_edtion = database.Column(database.String(36), primary_key='True')    
    id_edtion = database.Column(database.String(36), name="id_edtion", primary_key=True, default=generate_uuid)
    isbn = database.Column(database.String(13))
    nedtion = database.Column(database.Integer)
    volume = database.Column(database.Integer)
    printnumber = database.Column(database.Integer)
    tome = database.Column(database.String(10))
    year = database.Column(database.Integer)
    length = database.Column(database.Float)
    width = database.Column(database.Float)
    height = database.Column(database.Float)
    pages = database.Column(database.Integer)
    subject = database.Column(database.String(20))
    language = database.Column(database.String(20))
    bookbinding = database.Column(database.String(10))
    publisher = database.Column(database.String(20))
    synopsis = database.Column(database.String(2000))
    fk_tb_book_id = database.Column(database.String(36), database.ForeignKey('tb_book.id_book'))
    #books = database.relationship('BookModel')


    def __init__(self, isbn, nedtion, volume, printnumber, tome, year, length, width, height, pages, subject, language, bookbinding, publisher, synopsis, fk_tb_book_id):  
        #self.id_edtion = id_edtion
        self.isbn = isbn
        self.nedtion = nedtion
        self.volume = volume
        self.printnumber = printnumber
        self.tome = tome
        self.year = year
        self.length = length
        self.width = width
        self.height = height
        self.pages = pages
        self.subject = subject
        self.language = language
        self.bookbinding = bookbinding
        self.publisher = publisher
        self.synopsis = synopsis
        self.fk_tb_book_id = fk_tb_book_id

    def json(self):
        return {
                'id_edtion': self.id_edtion,
                'isbn': self.isbn,
                'nedtion': self.nedtion,
                'volume': self.volume,
                'printnumber': self.printnumber,
                'tome': self.tome,
                'year': self.year,
                'length': self.length,
                'width': self.width,
                'height': self.height,
                'pages': self.pages,
                'subject': self.subject,
                'language': self.language,
                'bookbinding': self.bookbinding,
                'publisher': self.publisher,
                'synopsis': self.synopsis,
                'fk_tb_book_id': self.fk_tb_book_id
        }

    @classmethod
    def find(cls, id_edtion):
        edtion = cls.query.filter_by(id_edtion = id_edtion).first()
        if edtion:
            return edtion
        return None
    
    def save(self):
        database.session.add(self)
        database.session.commit()

    def update(self, id_edtion, isbn, nedtion, volume, printnumber, tome, year, length, width, height, pages, subject, language, bookbinding, publisher, synopsis, fk_tb_book_id):  
        self.id_edtion = id_edtion
        self.isbn = isbn
        self.nedtion = nedtion
        self.volume = volume
        self.printnumber = printnumber
        self.tome = tome
        self.year = year
        self.length = length
        self.width = width
        self.height = height
        self.pages = pages
        self.subject = subject
        self.language = language
        self.bookbinding = bookbinding
        self.publisher = publisher
        self.synopsis = synopsis
        self.fk_tb_book_id = fk_tb_book_id

    def delete(self):
        database.session.delete(self)
        database.session.commit()