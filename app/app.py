from flask import Flask, jsonify
from flask_restful import Api
from resources.author import Author, Authors
from resources.book import Books, Book
from resources.edtion import Edtion, Edtions
from resources.book_author import BooksAuthors
from resources.user import User, UserRegister, UserAuth, UserLogout
from resources.estantevirtual import EVBook, EVBooks
from resources.auth import AuthMeli
from flask_jwt_extended import JWTManager
from db import Database
from blacklist import BLACKLIST

app = Flask(__name__)
#app.run(host='0.0.0.0', port=8080)

rdbms = ''
db_config = Database(rdbms)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boowk.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = db_config.getconfig()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admxz.82@35.202.33.13:3306/boowk'
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

#auth resource
api.add_resource(AuthMeli, '/auth')

#estantevirtual resources
api.add_resource(EVBooks, '/estantevirtual')

#book resources
api.add_resource(Books, '/books')       
api.add_resource(BooksAuthors, '/books')       
api.add_resource(Book, '/books/<string:id_book>')   

#users resources
api.add_resource(User, '/users/<string:login>')       
api.add_resource(UserRegister, '/users/register')    
api.add_resource(UserAuth, '/authorization')    
api.add_resource(UserLogout, '/logout') 

#author resources
api.add_resource(Authors, '/authors')
api.add_resource(Author, '/authors/<string:id_author>')    

#edtions resources
api.add_resource(Edtions, '/edtions')
api.add_resource(Edtion, '/edtions/<string:id_edtion>')    

#api.add_resource(BooksAuthors, '/books')


if __name__ == "__main__":
    from db import database
    database.init_app(app)    
    app.run(debug=True)