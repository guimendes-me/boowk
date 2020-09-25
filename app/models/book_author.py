from db import database
from .author import AuthorModel

class BookAuthorModel(database.Model):

    __tablename__ = 'ass_book_author'
    fk_tb_book_id = database.Column(database.String(36), database.ForeignKey('tb_book.id_book'), primary_key=True)
    fk_tb_author_id = database.Column(database.String(36), database.ForeignKey('tb_author.id_author'), primary_key=True)
    #books = database.relationship("BookModel", back_populates="tb_books")
    authors = database.relationship("AuthorModel")

    def __init__(self, book, author):
        self.fk_tb_book_id = book.id_book
        self.fk_tb_author_id = author.id_author

    def find(self):
        book_author = self.query.filter_by(fk_tb_book_id=self.fk_tb_book_id, fk_tb_author_id=self.fk_tb_author_id).first()
        return book_author

    def save(self):
        database.session.add(self)
        database.session.commit()
        

