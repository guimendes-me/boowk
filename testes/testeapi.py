import requests
import json

#dicionário com as informações de autenticação

base_url='http://34.95.216.159:8080'

data = {
    "username": "gmonteiro",
    "password": "teste123",
    "firstname": "Guilherme",
    "lastname": "Monteiro",
}

#dicionário que sera passado na requisição do token
credentials = {
    "username": data["username"],
    "password": data["password"]
}

#post na endpoint que valida as credenciais e retona o token
auth = requests.post(f'{base_url}/authorization', data=credentials)
print(auth.status_code)

#caso o usuário não exista (status code 401), ele é criado no endpoint register e em seguida o token é recuperado
if auth.status_code == 401:    
    response = requests.post(url=f'{base_url}/users/register', data=data)
    auth = requests.post(f'{base_url}/authorization', data=credentials)

#exibe o token que foi colocado no cabeçalho da próxima requisição
access_token = auth.json()['access_token']
headers={'Authorization': f'Bearer {access_token}' }
print(headers)


#lista que irá armazenar a reposta
authors = []

#lista de autores que será enviada
authors_json = {
            "firstname": "Brad",                
            "lastname": "Stone"
        }

for author_json in authors_json:
    print(author_json)
    post_author = requests.post(url=f'{base_url}/authors', data=author_json, headers=headers)
    print(post_author.status_code)
    print(post_author.json())
    authors.append(post_author.json())


#após ter cadastrado os autores, é possível cadastrar o livro e a lista de autores do mesmo
book_json = {
    "title": "A loja de tudo",
    "subtitle" : "Jeff Bezos e a era da Amazon",
    "booktype": "Livro",    
    "authors": authors_json

}

print(book_json)

post_book = requests.post(url=f'{base_url}/books', json=book_json, headers=headers)
print(post_book.status_code)
print(post_book.json())



#após efetuar o cadastro do livro, usamos o seu id para efetuar o cadastro da edição
edtions = requests.get(f'{base_url}/edtions')
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


post_edtion = requests.post(url=f'{base_url}/edtions', data=edtion_json, headers=headers)
print(post_edtion.status_code)
print(post_edtion.json())

