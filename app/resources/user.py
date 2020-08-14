from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from models.user import UserModel
from blacklist import BLACKLIST

arguments = reqparse.RequestParser()
arguments.add_argument('login', type=str, required=True, help=" The field 'login' connot be left blank")
arguments.add_argument('password', type=str, required=True, help=" The field 'password' connot be left blank")
arguments.add_argument('firstname', type=str)
arguments.add_argument('lastname', type=str)
        
class User(Resource):

    def get(self, login):        
        user = UserModel.find(login)
        if user:
            return user.json()

        return {'message': 'User not found.'}, 404
        
    @jwt_required        
    def delete(self, login):
        
        user = UserModel.find(login)

        if user:
            try:
                user.delete()
            except:
                return {'mensage': 'An error ocurred trying to delete user.'}, 500
                
            return {'mensage': 'User deleted'}

        return {'mensage': 'User not found'}, 404            

class UserRegister(Resource):


    def post(self):
        data = arguments.parse_args()    

        if UserModel.find(data['login']):
            return {'mensage': "The login '{}' alredy exists".format(data['login'])}

        user = UserModel(**data)
        user.save()
        
        return {'mensage': "The user '{}' created sucessfully!".format(data['login'])}, 201


class UserAuth(Resource):        

    @classmethod
    def post(cls):
        dados = arguments.parse_args()
        user = UserModel.find(dados['login'])
        
        if user and safe_str_cmp(user.password, dados['password']):
            acess_token = create_access_token(identity=user.user_id)
            return {'acess_token': acess_token}, 200
        
        return {'mensage': 'The username or password is incorrect.'}, 401

class UserLogout(Resource):
    
    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out sucessfully !'}, 200
