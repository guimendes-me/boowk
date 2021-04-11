from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from models.credential import CredentialModel
from blacklist import BLACKLIST

arguments = reqparse.RequestParser()
arguments.add_argument('fk_username', type=str, required=True, help=" The field 'username' connot be left blank")
arguments.add_argument('ev_email', type=str)
arguments.add_argument('ev_password', type=str)


class Credential(Resource):

    @jwt_required
    def get(self, username):        
        user = CredentialModel.find(username)
        if user:        
            return {"credentials": user.json()}, 200
        return {"credentials": None}, 404

class Credentials(Resource):

    @jwt_required
    def post(self):
        data = arguments.parse_args()    

        if CredentialModel.find(data["fk_username"]):
            return {'mensage': "The credentials of '{}' alredy exists".format(data["fk_username"])}, 203
        else:
            user = CredentialModel(**data)
            user.save()        
            return {'mensage': "The credentials of '{}' created sucessfully!".format(data["fk_username"])}, 201    