from models.estantevirtual import EVBookModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask import Flask, request
import uuid

class EVBooks(Resource):

    arguments = reqparse.RequestParser()            
    arguments.add_argument('uuid_ev', type=str, required=True, help=" The field 'titulo' connot be left blank")    
    arguments.add_argument('erro', type=str, required=False)
    arguments.add_argument('isbn_issn', type=str, required=False)
    arguments.add_argument('autor', type=str, required=False)
    arguments.add_argument('titulo', type=str, required=False)
    arguments.add_argument('editora', type=str, required=False)
    arguments.add_argument('ano', type=int, required=False)
    arguments.add_argument('estante', type=str, required=False)
    arguments.add_argument('preco', type=float, required=False)
    arguments.add_argument('conservacao', type=str, required=False)
    arguments.add_argument('peso', type=float, required=False)
    arguments.add_argument('tipo_publicacao', type=str, required=False)
    arguments.add_argument('tipo_produto', type=str, required=False)
    arguments.add_argument('edicao_numero', type=int, required=False)
    arguments.add_argument('numero', type=int, required=False)
    arguments.add_argument('idioma', type=str, required=False)
    arguments.add_argument('volume', type=str, required=False)
    arguments.add_argument('acabamento', type=str, required=False)
    arguments.add_argument('desconto', type=float, required=False)
    arguments.add_argument('marcas_de_uso', type=str, required=False)
    arguments.add_argument('amarelo', type=str, required=False)
    arguments.add_argument('manchas_bolor', type=str, required=False)
    arguments.add_argument('grifos_anotacoes', type=str, required=False)
    arguments.add_argument('amassados_orelha', type=str, required=False)
    arguments.add_argument('rasgos', type=str, required=False)
    arguments.add_argument('dedicatoria', type=str, required=False)
    arguments.add_argument('autografo', type=str, required=False)
    arguments.add_argument('numeric_id', type=int, required=False)
    arguments.add_argument('assunto', type=str, required=False)
    arguments.add_argument('localizacao', type=str, required=False)
    arguments.add_argument('seller', type=str, required=False)
    
    
    #@jwt_required
    def get(self):
        return {'books': [book.json() for book in EVBookModel.query.all()]}
    
    @jwt_required
    def post(self):        
                
        ev_data = self.arguments.parse_args()
        ev_book = EVBookModel(**ev_data)
        ev_find = ev_book.find(ev_data.titulo)

        if ev_find:
            #return {"mensage": "Book id '{}' already exists.".format(data.titulo)}, 200
            return ev_find.json(), 409
        else:            
            try:
                ev_book.save()
            except:
                return {'mensage': 'An internal error ocurred trying to save ev.'}, 500
            return ev_book.json()


class EVBook(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('titulo', type=str, required=True, help=" The field 'titulo' connot be left blank")        


    def get(self, uuid_ev):        
        book = EVBookModel.find(uuid_ev)
        if book:
            return book.json()

        return {'message': 'Book not found.'}, 404

    
    @jwt_required
    def put(self, id_book):

        data = EVBook.arguments.parse_args()        
        book_obj =  EVBookModel(**data)

        #data = BookModel.find(field='id_book', key=id_book)                
        
        try:
            
            if book_obj.find(field='id_book', key=id_book):
                book_obj.update(**data)
                book_obj.save()
                return book_obj.json(), 200 #ok
            else:

                if book_obj.find(book_obj.titulo):
                    book_obj = book_obj.find(book_obj.titulo)
                    return  book_obj.json(), 409
                else:
                    book_obj.save()
                    return book_obj.json(), 200
        except:
            return {'mensage': 'An internal error ocurred trying to save book.'}, 500
            
        

        
    @jwt_required
    def delete(self, uuid_ev):
        
        book = EVBookModel.find(field='uuid_ev', key=uuid_ev)

        if book:
            try:
                book.delete()
            except:
                return {'mensage': 'An error ocurred trying to delete book.'}, 500
                
            return {'mensage': 'Livro deletado'}

        return {'mensage': 'Book not found'}, 404            