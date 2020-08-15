from flask import Flask, jsonify
from flask_restful import Api
from resources.book import Books, Book
from resources.user import User, UserRegister, UserAuth, UserLogout
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)
app.run(host='0.0.0.0', port=8080)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'ArrowCaraiLoko'
app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)
jwt =  JWTManager(app)

@app.before_first_request
def create_database():
    database.create_all()


@jwt.token_in_blacklist_loader
def check_blacklist(token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def revoke_token():
    return jsonify({'mensage': 'You have been logged out.'}), 401

api.add_resource(Books, '/books')       
api.add_resource(Book, '/books/<int:book_id>')       
api.add_resource(User, '/users/<string:login>')       
api.add_resource(UserRegister, '/users/register')    
api.add_resource(UserAuth, '/authorization')    
api.add_resource(UserLogout, '/logout') 

if __name__ == '__main__':
    from db import database
    database.init_app(app)
    app.run(debug=True)