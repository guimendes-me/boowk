from flask_restful import Resource, reqparse
from models.book import BookModel
from models.author import AuthorModel
from models.edtion import EdtionModel
from flask_jwt_extended import jwt_required
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import uuid
db = SQLAlchemy()


path_parameters =  reqparse.RequestParser()
path_parameters.add_argument('title', type=str)
path_parameters.add_argument('limit', type=float)
path_parameters.add_argument('offset', type=float)

def normalize_path(title=None, limit=30, offset=0, **dados):
    
    if title:
        return {
            'title': title,
            'limit': limit,
            'offset': offset
        }
    
    return {                             
            'limit': limit,
            'offset': offset
        }

class Books(Resource):

    arguments = reqparse.RequestParser()    
    arguments.add_argument('title', type=str, required=True, help=" The field 'title' connot be left blank")
    arguments.add_argument('subtitle', type=str, required=True)
    arguments.add_argument('booktype', type=str, required=True)    
    '''    
    def get(self):
        return {'books': [book.json() for book in BookModel.query.all()]}
    '''

    def get(self):


        data = path_parameters.parse_args()
        valid_data = {key:data[key] for key in data if data[key] is not None}
        parameters = normalize_path(**valid_data)

        if not parameters.get('title'):
            query = '''
                    SELECT  
                        bk.id_book                
                    FROM tb_book bk                   
                        LIMIT :limit 
                        OFFSET :offset'''
            result = db.engine.execute(text(query), limit=parameters['limit'], offset=parameters['offset'])
            
        else: 
            query = '''
                    SELECT  
                        bk.id_book                  
                    FROM tb_book bk
                        WHERE bk.title = :title 
                        LIMIT :limit 
                        OFFSET :offset'''
            result = db.engine.execute(text(query), title=parameters['title'], limit=parameters['limit'], offset=parameters['offset'])
        
        books = []

        for row in result:     
            bookmodel = BookModel.find(key=row[0], field='id_book')
            books.append(bookmodel.json())
            
        return {'books': books}


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
    def put(self, id_book):

        data = Book.arguments.parse_args()
        
        book_obj =  BookModel(**data)

        #data = BookModel.find(field='id_book', key=id_book)                
        
        try:
            
            if book_obj.find(field='id_book', key=id_book):
                book_obj.update(**data)
                book_obj.save()
                return book_obj.json(), 200 #ok
            else:

                if book_obj.find(book_obj.title):
                    book_obj = book_obj.find(book_obj.title)
                    return  book_obj.json(), 409
        except:
            return {'mensage': 'An internal error ocurred trying to save book.'}, 500
            
        

        
    @jwt_required
    def delete(self, id_book):
        
        book = BookModel.find(field='id_book', key=id_book)

        if book:
            try:
                book.delete()
            except:
                return {'mensage': 'An error ocurred trying to delete book.'}, 500
                
            return {'mensage': 'Livro deletado'}

        return {'mensage': 'Book not found'}, 404            