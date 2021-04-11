from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from models.user import UserModel
from blacklist import BLACKLIST
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from models.seller import SellerModel
import uuid
db = SQLAlchemy()


path_parameters =  reqparse.RequestParser()
path_parameters.add_argument('url', type=str)
path_parameters.add_argument('limit', type=float)
path_parameters.add_argument('offset', type=float)

def normalize_path(url=None, limit=30, offset=0, **dados):
    
    if url:
        return {
            'url': url,
            'limit': limit,
            'offset': offset
        }
    
    return {                             
            'limit': limit,
            'offset': offset
        }

class Sellers(Resource):

    arguments = reqparse.RequestParser()    
    arguments.add_argument('url', type=str, required=True, help=" The field 'url' connot be left blank")        

    #@jwt_required
    def get(self):

        data = path_parameters.parse_args()
        valid_data = {key:data[key] for key in data if data[key] is not None}
        parameters = normalize_path(**valid_data)

        if not parameters.get('url'):
            query = '''
                    SELECT  
                        sl.url               
                    FROM scraper.seller sl                  
                        LIMIT :limit 
                        OFFSET :offset'''
            result = db.engine.execute(text(query), limit=parameters['limit'], offset=parameters['offset'])
            
        else: 
            query = '''
                    SELECT  
                        sl.url               
                    FROM scraper.seller sl  
                        WHERE sl.url  = :url 
                        LIMIT :limit 
                        OFFSET :offset'''
            result = db.engine.execute(text(query), title=parameters['url'], limit=parameters['limit'], offset=parameters['offset'])
        
        sellers = []

        for row in result:     
            sellermodel = SellerModel.find(row[0])
            sellers.append(sellermodel.json())
            
        return {'sellers': sellers}


    @jwt_required
    def post(self):
        data = self.arguments.parse_args()        
        seller = SellerModel(**data)
        seller_find = seller.find(seller.url)

        if seller_find:
            #return {"mensage": "Book id '{}' already exists.".format(data.title)}, 200
            return seller_find.json(), 409
        else:            
            try:
                seller.save()
            except:
                return {'mensage': 'An internal error ocurred trying to save author.'}, 500
            return seller.json()


class Seller(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('name', type=str, required=True, help=" The field 'title' connot be left blank")


    def get(self, name):        
        seller = SellerModel.find(name)
        if seller:
            return seller.json()

        return {'message': 'Book not found.'}, 404         

        
    @jwt_required
    def delete(self, name):
        
        seller = SellerModel.find(name)

        if seller:
            try:
                seller.delete()
            except:
                return {'mensage': 'An error ocurred trying to delete seller.'}, 500
                
            return {'mensage': 'Seller deletado'}

        return {'mensage': 'Seller not found'}, 404            