from flask_restful import Resource, reqparse
from models.author import AuthorModel
from flask_jwt_extended import jwt_required
import uuid

class Authors(Resource):

    def get(self):
        return {'authors': [author.json() for author in AuthorModel.query.all()]}
        


class Author(Resource):
    
    arguments = reqparse.RequestParser()
    arguments.add_argument('firstname', type=str, required=True, help=" The field 'firstname' connot be left blank")
    arguments.add_argument('middlename', type=str)
    arguments.add_argument('lastname', type=str, required=True, help=" The field 'lastname' connot be left blank")


    @jwt_required
    def post(self):
        data = self.arguments.parse_args()        
        author = AuthorModel(**data)
        author_find = author.find(author.firstname)

        if author_find:
            #return {"mensage": "Book id '{}' already exists.".format(data.title)}, 200
            return author_find.json(), 409
        else:            
            try:
                author.save()
            except:
                return {'mensage': 'An internal error ocurred trying to save book.'}, 500
            return author.json()

