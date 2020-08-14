from flask_restful import Resource, reqparse
from models.book import BookModel
from flask_jwt_extended import jwt_required

class Books(Resource):

    def get(self):
        return {'books': [book.json() for book in BookModel.query.all()]}


class Book(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('title', type=str, required=True, help=" The field 'title' connot be left blank")
    arguments.add_argument('author', type=str, required=True, help=" The field 'author' connot be left blank")


    def get(self, book_id):        
        book = BookModel.find(book_id)
        if book:
            return book.json()

        return {'message': 'Book not found.'}, 404

    @jwt_required
    def post(self, book_id):
        
        if BookModel.find(book_id):
            return {"mensage": "Book id '{}' already exists.".format(book_id)}, 200

        data = Book.arguments.parse_args()
        book = BookModel(book_id, **data)
        try:
            book.save()
        except:
            return {'mensage': 'An internal error ocurred trying to save book.'}, 500
        return book.json()
    
    @jwt_required
    def put(self, book_id):

        data = Book.arguments.parse_args()
        book_model =  BookModel(book_id, **data)

        find_book = BookModel.find(book_id)                

        if find_book:
            find_book.update(**data)
            find_book.save()
            return find_book.json(), 200 #ok
        
        new_book = BookModel(book_id, **data)
        
        try:
            new_book.save()
        except:
            return {'mensage': 'An internal error ocurred trying to save book.'}, 500
        return book.json()
        
    @jwt_required
    def delete(self, book_id):
        
        book = BookModel.find(book_id)

        if book:
            try:
                book.delete()
            except:
                return {'mensage': 'An error ocurred trying to delete book.'}, 500
                
            return {'mensage': 'Livro deletado'}

        return {'mensage': 'Book not found'}, 404            