from db import database

class BookModel(database.Model):
    __tablename__ = 'books'

    book_id = database.Column(database.Integer, primary_key='True')
    title = database.Column(database.String(100))
    author = database.Column(database.String(50))


    def __init__(self, book_id, title, author):  
        self.book_id = book_id
        self.title = title
        self.author = author

    def json(self):
        return {
            'book_id': self.book_id,
            'title': self.title,            
            'author' : self.author
        }

    @classmethod
    def find(cls, book_id):
        book = cls.query.filter_by(book_id = book_id).first()
        if book:
            return book
        return None
    
    def save(self):
        database.session.add(self)
        database.session.commit()

    def update(self, title, author):
        self.title = title
        self.author = author

    def delete(self):
        database.session.delete(self)
        database.session.commit()