from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask import Flask, request


def normalize_path_params(code):
    return code

path_params = reqparse.RequestParser()
path_params.add_argument('code', type=str)

class AuthMeli(Resource):

    def get(self):
        code = path_params.parse_args()

        if code['code'] is None:
            code['code'] = 'Vazio'
        
        return {'auth': code['code']}    