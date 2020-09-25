from flask_restful import Resource, reqparse
from models.edtion import EdtionModel
from flask_jwt_extended import jwt_required
import uuid
import sqlite3

path_parameters =  reqparse.RequestParser()
path_parameters.add_argument('isbn', type=str)
path_parameters.add_argument('nedtion', type=str)
path_parameters.add_argument('min_year', type=str)
path_parameters.add_argument('max_year', type=str)
path_parameters.add_argument('limit', type=float)
path_parameters.add_argument('offset', type=float)

def normalize_path(isbn=None, limit=30, offset=0, **dados):
    
    if isbn:
        return {
            'isbn': isbn,
            'limit': limit,
            'offset': offset
        }
    
    return {                             
            'limit': limit,
            'offset': offset
        }

class Edtions(Resource):
 

    def get(self):
        
        connection = sqlite3.connect('boowk.db')
        cursor = connection.cursor()

        data = path_parameters.parse_args()
        valid_data = {key:data[key] for key in data if data[key] is not None}
        parameters = normalize_path(**valid_data)

        if not parameters.get('isbn'):
            query = "SELECT * FROM tb_edtion LIMIT ? OFFSET ?"
            filters = tuple(parameters[chave] for chave in parameters)
            #filters = (parameters['limit'], parameters['offset'])
            result = cursor.execute(query, filters)
            
        else: 
            query = "SELECT * FROM tb_edtion WHERE isbn = ? LIMIT ? OFFSET ?"
            filters = tuple(parameters[chave] for chave in parameters)
            result = cursor.execute(query, filters)

        edtions = []
        
        for row in result:
            edtions.append(
                {        
                'id_edtion': row[0],
                'isbn': row[1],
                'nedtion': row[2],
                'volume': row[3],
                'printnumber': row[4],
                'tome': row[5],
                'year': row[6],
                'length': row[7],
                'width': row[8],
                'height': row[9],
                'pages': row[10],
                'subject': row[11],
                'language': row[12],
                'bookbinding': row[13],
                'publisher': row[14],
                'synopsis': row[15],
                'fk_tb_book_id': row[16]
                }
        )

        return {'edtions': edtions}


class Edtion(Resource):

    arguments = reqparse.RequestParser()    
    arguments.add_argument('isbn', type=str)
    arguments.add_argument('nedtion', type=str)
    arguments.add_argument('volume', type=str)
    arguments.add_argument('printnumber', type=str)
    arguments.add_argument('tome', type=str)
    arguments.add_argument('year', type=str)
    arguments.add_argument('length', type=str)
    arguments.add_argument('width', type=str)
    arguments.add_argument('height', type=str)
    arguments.add_argument('pages', type=str)
    arguments.add_argument('subject', type=str)
    arguments.add_argument('language', type=str)
    arguments.add_argument('bookbinding', type=str)
    arguments.add_argument('publisher', type=str)
    arguments.add_argument('synopsis', type=str)
    arguments.add_argument('fk_tb_book_id', type=str)
    
    #arguments.add_argument('author', type=str, required=True, help=" The field 'author' connot be left blank")


    def get(self, edtion_id):        
        edtion = EdtionModel.find(edtion_id)
        if edtion:
            return edtion.json()

        return {'message': 'Edtion not found.'}, 404


    @jwt_required
    def post(self):

        """
        edtion_id = str(uuid.uuid1())
        
        if EdtionModel.find(edtion_id):
            return {"mensage": "Edtion id '{}' already exists.".format(edtion_id)}, 200
        

        while EdtionModel.find(edtion_id):
            edtion_id = str(uuid.uuid1())
        """

        data = Edtion.arguments.parse_args()
        edtion = EdtionModel(**data)
        try:
            edtion.save()
        except:
            return {'mensage': 'An internal error ocurred trying to save book.'}, 500
        return edtion.json()
