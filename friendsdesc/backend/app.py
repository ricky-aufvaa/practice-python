from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#we'll create a db 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///friends.db"
db = SQLAlchemy(app)


#define the schema 
class Friend(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(300), nullable = False)
    role = db.Column(db.String(300), nullable = True)

    def to_json(self):
        return {
            "id": self.id,
            "role": self.role
        }

#routes
@app.route("/api/friend", methods = ['GET'])
def view():
    friends = Friend.query.all()
    results = [friend.to_json() for friend in friends]
    return jsonify(results)

@app.route("/api/friend", methods = ["POST"])
def create_friend():
    data = request.json
    name = data.get("name")
    role = data.get("role")
    new_friend = Friend(name = name, role =role )

    db.session.add(new_friend)
    db.session.commit()

    return "friend create successfully. "

with app.app_context():
    db.create_all()
if __name__ == ("__main__"):
    app.run(debug = True)