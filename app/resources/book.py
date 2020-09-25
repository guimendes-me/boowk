from flask_restful import Resource, reqparse
from models.book import BookModel
from models.author import AuthorModel
from flask_jwt_extended import jwt_required
from flask import Flask, request
import uuid

class Books(Resource):

    arguments = reqparse.RequestParser()
    

    arguments.add_argument('title', type=str, required=True, help=" The field 'title' connot be left blank")
    arguments.add_argument('subtitle', type=str, required=True)
    arguments.add_argument('booktype', type=str, required=True)    
    
    
    def get(self):
        return {'books': [book.json() for book in BookModel.query.all()]}
    '''
    @jwt_required
    def post(self):        
                
        book_data = self.arguments.parse_args()
        book = BookModel(**book_data)
        book_find = book.find(book.title)

        if book_find:
            #return {"mensage": "Book id '{}' already exists.".format(data.title)}, 200
            return book_find.json(), 409
        else:            
            try:
                book.save()
            except:
                return {'mensage': 'An internal error ocurred trying to save book.'}, 500
            return book.json()
    '''

class Book(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('title', type=str, required=True, help=" The field 'title' connot be left blank")
    arguments.add_argument('subtitle', type=str, required=True)
    arguments.add_argument('booktype', type=str, required=True)
    


    def get(self, id_book):        
        book = BookModel.find(id_book)
        if book:
            return book.json()

        return {'message': 'Book not found.'}, 404

    
    @jwt_required
    def put(self, book_id):

        data = Book.arguments.parse_args()
        data =  BookModel(book_id, **data)

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
        return find_book.json()
        
    #@jwt_required
    def delete(self, id_book):
        
        book = BookModel.find(field='id_book', key=id_book)

        if book:
            try:
                book.delete()
            except:
                return {'mensage': 'An error ocurred trying to delete book.'}, 500
                
            return {'mensage': 'Livro deletado'}

        return {'mensage': 'Book not found'}, 404            