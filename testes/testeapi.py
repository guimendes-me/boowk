import requests
import json

data = {
    "login": "gmendes",
    "password": "teste123",
    "firstname": "Guilherme",
    "lastname": "Monteiro"
}

credentials = {
    "login": data["login"],
    "password": data["password"]
}

auth = requests.post('http://127.0.0.1:5000/authorization', data=credentials)
print(auth.status_code)

if auth.status_code == 401:    
    response = requests.post(url='http://127.0.0.1:5000/users/register', data=data)
    auth = requests.post('http://127.0.0.1:5000/authorization', data=credentials)

access_token = auth.json()['access_token']
headers={'Authorization': f'Bearer {access_token}' }
print(headers)



authors = []

authors_json = {
            "firstname": "Brad",                
            "lastname": "Stone"
        }, {
            "firstname": "Seth",             
            "lastname": "Godin"
        }



'''
for author_json in authors_json:
    print(author_json)
    post_author = requests.post(url='http://127.0.0.1:5000/authors', data=author_json, headers=headers)
    print(post_author.status_code)
    print(post_author.json())
    authors.append(post_author.json())

'''


book_json = {
    "title": "A loja de tudo",
    "subtitle" : "Jeff Bezos e a era da Amazon",
    "booktype": "Livro",    
    "authors": authors_json

}

print(book_json)

post_book = requests.post(url='http://127.0.0.1:5000/books', json=book_json, headers=headers)
print(post_book.status_code)
print(post_book.json())




edtions = requests.get('http://127.0.0.1:5000/edtions')
edtion_json = {
    "isbn": "9788551004739",
    "nedtion": 1,
    "volume": 1,
    "printnumber": 1,
    "tome": None,
    "year": 2019,
    "length": 2.2,
    "width": 16,
    "height": 23,
    "pages": 400,
    "subject": "Biografias",
    "language": "Português",
    "bookbinding": "Brochura",
    "publisher": "Intrínseca ",
    "synopsis": "Pioneira no comércio de livros pela internet, a Amazon esteve à frente da primeira grande febre das pontocom. \
    Mas Jeff Bezos, seu visionário criador, não se contentaria com uma livraria virtual descolada: ele queria que a Amazon dispusesse de \
    uma seleção ilimitada de produtos a preços radicalmente baixos – e se tornasse “a loja de tudo”. Para pôr em prática essa visão, Bezos \
    desenvolveu uma cultura corporativa de ambição implacável e alto sigilo que poucos conheciam de verdade.",
    "fk_tb_book_id": post_book.json()['book']['id_book']
    }

#print(edtion_json)


post_edtion = requests.post(url='http://127.0.0.1:5000/edtions', data=edtion_json, headers=headers)
print(post_edtion.status_code)
print(post_edtion.json())


post_edtion = requests.post(url='http://127.0.0.1:5000/edtions', data=edtion_json, headers=headers)
print(post_edtion.status_code)
print(post_edtion.json())