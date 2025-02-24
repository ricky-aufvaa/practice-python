from app import db
#implementing the scheme of my db

class Friend(db.Model):
    name = db.Column(db.String(100), nullable = False) 
