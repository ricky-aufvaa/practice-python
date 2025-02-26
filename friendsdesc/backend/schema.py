from app import db

#define the schema 
class Friend(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(300), nullable = False)
    role = db.Column(db.String(300), nullable = True)

    def to_json(self):
        return {
            "name": self.name,
            "role": self.role
        }