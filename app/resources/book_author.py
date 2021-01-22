from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from webargs import fields, validate
from models.book import BookModel
from models.author import AuthorModel
from models.book_author import BookAuthorModel, BookAuthorModel
import ast



class BooksAuthors(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('title', type=str, required=True, help=" The field 'title' connot be left blank")
    arguments.add_argument('subtitle', type=str, required=True)
    arguments.add_argument('booktype', type=str, required=True)    
    arguments.add_argument('authors', type=str, action='append', required=True)

    @jwt_required
    def post(self):

        items = self.arguments.parse_args()
        
        authors = [ast.literal_eval(authors) for authors in items['authors']]        
        authors_obj = []

        for author in authors:
            if author.get('middlename'):
                authors_obj.append(AuthorModel(**author))
            else:
                author['middlename'] = None
                authors_obj.append(AuthorModel(**author))
                        
        items.pop('authors')
        book_obj = BookModel(**items)
        
        if book_obj.find(book_obj.title):
            book_obj = book_obj.find(book_obj.title)
            return {'book': book_obj.json()}, 409

        else:
            book_obj.save()
            for author_obj in authors_obj:

                if not author_obj.find(author_obj.firstname):
                    author_obj.save()                  
                else:
                    author_obj = author_obj.find(author_obj.firstname)
                
                book_author_obj = BookAuthorModel(book_obj, author_obj)
                            
                if not book_author_obj.find():
                    book_author_obj.save()  
            
        
            return {'book': book_obj.json()}, 200
            
            #book_author_obj.save()
             
            
        #return {'title': items['title'], 'subtitle': items['subtitle'], 'authors': items}
        #return {'book': book_obj.json(), 'authors': authors_json}
        #return {'book': book_obj.json(), 'teste': author_obj.json()}
