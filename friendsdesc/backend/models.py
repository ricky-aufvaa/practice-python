from app import db
#implementing the scheme of my db

class Friend(db.Model):
    name = db.Column(db.String(100), nullable = False) 
    role = db.Column(db.String(50), nullable = False)

def to_json(self):
    return
    {
        "name": self.name,
        "role": self.role
    }