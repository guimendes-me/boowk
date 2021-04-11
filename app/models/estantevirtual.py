from db import database, Database
import uuid

class EVBookModel(database.Model):

    #book_author = BooksAuthorsModel()

    def generate_uuid(self):
        return str(uuid.uuid1())

    __tablename__ = 'tb_evestantevirtual'
    uuid_ev = database.Column(database.String(40), primary_key=True)
    erro = database.Column(database.String(100))
    isbn_issn = database.Column(database.String(100))
    autor = database.Column(database.String(200))
    titulo = database.Column(database.String(300))
    editora = database.Column(database.String(100))
    ano = database.Column(database.Integer)
    estante = database.Column(database.String(100))
    preco = database.Column(database.Float)
    conservacao = database.Column(database.String(8000))
    peso = database.Column(database.Float)
    tipo_publicacao = database.Column(database.String(100))
    tipo_produto = database.Column(database.String(100))
    edicao_numero = database.Column(database.Integer)
    numero = database.Column(database.Integer)
    idioma = database.Column(database.String(100))
    volume = database.Column(database.String(100))
    acabamento = database.Column(database.String(100))
    desconto = database.Column(database.Float)
    marcas_de_uso = database.Column(database.String(100))
    amarelo = database.Column(database.String(100))
    manchas_bolor = database.Column(database.String(100))
    grifos_anotacoes = database.Column(database.String(100))
    amassados_orelha = database.Column(database.String(100))
    rasgos = database.Column(database.String(100))
    dedicatoria = database.Column(database.String(100))
    autografo = database.Column(database.String(100))
    numeric_id = database.Column(database.String(100))
    assunto = database.Column(database.String(100))
    localizacao = database.Column(database.String(100))
    seller = database.Column(database.String(100))
    

    def __init__(self, uuid_ev, erro, isbn_issn, autor, titulo, editora, ano, estante, preco, conservacao, peso, tipo_publicacao, tipo_produto, edicao_numero, numero, idioma, volume, acabamento, desconto, marcas_de_uso, amarelo, manchas_bolor, grifos_anotacoes, amassados_orelha, rasgos, dedicatoria, autografo, numeric_id, assunto, localizacao, seller):          
        self.uuid_ev = uuid_ev
        self.erro = erro
        self.isbn_issn = isbn_issn
        self.autor = autor
        self.titulo = titulo
        self.editora = editora
        self.ano = ano
        self.estante = estante
        self.preco = preco
        self.conservacao = conservacao
        self.peso = peso
        self.tipo_publicacao = tipo_publicacao
        self.tipo_produto = tipo_produto
        self.edicao_numero = edicao_numero
        self.numero = numero
        self.idioma = idioma
        self.volume = volume
        self.acabamento = acabamento
        self.desconto = desconto
        self.marcas_de_uso = marcas_de_uso
        self.amarelo = amarelo
        self.manchas_bolor = manchas_bolor
        self.grifos_anotacoes = grifos_anotacoes
        self.amassados_orelha = amassados_orelha
        self.rasgos = rasgos
        self.dedicatoria = dedicatoria
        self.autografo = autografo
        self.numeric_id = numeric_id
        self.assunto = assunto
        self.localizacao = localizacao    
        self.seller = seller
        

    def json(self):
        return {
            "uuid_ev": self.uuid_ev,
            "erro": self.erro,
            "isbn_issn": self.isbn_issn,
            "autor": self.autor,
            "titulo": self.titulo,
            "editora": self.editora,
            "ano": self.ano,
            "estante": self.estante,
            "preco": self.preco,
            "conservacao": self.conservacao,
            "peso": self.peso,
            "tipo_publicacao": self.tipo_publicacao,
            "tipo_produto": self.tipo_produto,
            "edicao_numero": self.edicao_numero,
            "numero": self.numero,
            "idioma": self.idioma,
            "volume": self.volume,
            "acabamento": self.acabamento,
            "desconto": self.desconto,
            "marcas_de_uso": self.marcas_de_uso,
            "amarelo": self.amarelo,
            "manchas_bolor": self.manchas_bolor,
            "grifos_anotacoes": self.grifos_anotacoes,
            "amassados_orelha": self.amassados_orelha,
            "rasgos": self.rasgos,
            "dedicatoria": self.dedicatoria,
            "autografo": self.autografo,
            "numeric_id": self.numeric_id,
            "assunto": self.assunto,
            "localizacao": self.localizacao,
            "seller": self.seller
        }

    @classmethod
    def find(cls, key, field='titulo', like=True):        
        #book = cls.query.filter_by(id_book = id_book).first()
        
        if field=='titulo' and like==True:
            ev = cls.query.filter(EVBookModel.titulo.like(f'%{key}%')).first()
        if field=='uuid_ev':
            ev = cls.query.filter_by(id_book=key).first()
        if ev:
            return ev
        return None
        
    
    def save(self):           
        database.session.add(self)
        database.session.commit()

    def update(self, uuid_ev, erro, isbn_issn, auor, titulo, editora, ano, estante, preco, conservacao, peso, tipo_publicacao, tipo_produto, edicao_numero, numero, idioma, volume, acabamento, desconto, marcas_de_uso, amarelo, manchas_bolor, grifos_anotacoes, amassados_orelha, rasgos, dedicatoria, autografo, numeric_id, assunto, localizacao, seller):          
        self.uuid_ev = uuid_ev
        self.erro = erro
        self.isbn_issn = isbn_issn
        self.autor = autor
        self.titulo = titulo
        self.editora = editora
        self.ano = ano
        self.estante = estante
        self.preco = preco
        self.conservacao = conservacao
        self.peso = peso
        self.tipo_publicacao = tipo_publicacao
        self.tipo_produto = tipo_produto
        self.edicao_numero = edicao_numero
        self.numero = numero
        self.idioma = idioma
        self.volume = volume
        self.acabamento = acabamento
        self.desconto = desconto
        self.marcas_de_uso = marcas_de_uso
        self.amarelo = amarelo
        self.manchas_bolor = manchas_bolor
        self.grifos_anotacoes = grifos_anotacoes
        self.amassados_orelha = amassados_orelha
        self.rasgos = rasgos
        self.dedicatoria = dedicatoria
        self.autografo = autografo
        self.numeric_id = numeric_id
        self.assunto = assunto
        self.localizacao = localizacao    
        self.seller = seller

    def delete(self):
        database.session.delete(self)
        database.session.commit()
        return {"mensage": "Book not found"}            