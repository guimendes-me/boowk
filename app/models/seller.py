from db import database

class SellerModel(database.Model):
    __tablename__ = 'seller'
    __table_args__ = ({"schema": "scraper"})

    name = database.Column(database.String(30), primary_key=True)
    url = database.Column(database.String(200))
    store = database.Column(database.String(200))
    rating = database.Column(database.Float)
    ratings = database.Column(database.Float)    
    membersince = database.Column(database.Date)
    bookamount = database.Column(database.Integer)
    authentication = database.Column(database.String(20))
    

    def __init__(self, url):  
        self.name = url.replace('https://www.estantevirtual.com.br/livreiros/', '').replace('-', '')
        self.url = url


    def json(self):
        return {
        "name": self.name,
        "url": self.url,
        "store": self.store,
        "rating": self.rating,
        "ratings": self.ratings,
        "membersince": self.membersince,
        "bookamount": self.bookamount,
        "authentication": self.authentication
        }

    @classmethod
    def find(cls, url):
        seller = cls.query.filter_by(url = url).first()
        if seller:
            return seller
        return None
    
    def save(self):
        database.session.add(self)
        database.session.commit()

    def update(self, name, url, store, rating, ratings, membersince, bookamount, authentication):  
        self.name = name
        self.url = url
        self.store = store
        self.rating = rating
        self.ratings = ratings
        self.membersince = membersince
        self.bookamount = bookamount
        self.authentication = authentication

    def delete(self):
        database.session.delete(self)
        database.session.commit()