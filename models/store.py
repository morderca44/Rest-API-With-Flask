from db import db

class StoreModel(db.Model):    # db model tworzy cos w rodzaju mapy pomiedzy obiektami i bazą danych, db.model wskazuje,że te obiekty będą wchodziły w interakcje z bazą danych

    __tablename__= "stores"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name=name



    def json(self):
        return {"name": self.name, "items":[item.json() for item in self.items.all()]}



    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name =  name LIMIT 1, filter_by is a query builder

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



