from flask import request,jsonify

from app import app,db
from schema import Friend

#routes
@app.route('/')
def hello():
    return "hello"
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
    # new_friend = to_json(new_friend)
    return "friend create successfully. "