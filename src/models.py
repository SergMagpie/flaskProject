from src import db


class Events(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    asin = db.Column(db.String)
    brand = db.Column(db.String)
    id_code = db.Column(db.String)
    source = db.Column(db.String)
    stars = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)

    def __init__(self, asin, brand, id, source, stars, timestamp):
        self.asin = asin
        self.brand = brand
        self.id_code = id
        self.source = source
        self.stars = stars
        self.timestamp = timestamp
