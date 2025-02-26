from flask import request,jsonify

from app import app,db
from schema import Friend

@app.route("/api/friend", methods =["GET"] )
def show_friends():
    friends= Friend.query.all()
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
    json_return = Friend.to_json(new_friend)
    #typical API approach is returning a json
    return (json_return)