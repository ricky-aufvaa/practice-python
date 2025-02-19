#creating  a minimal hello world program using flask
from flask import Flask
#import module for rendering html
from flask import render_template
#using sql database using flask using sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'
#removing the track warnings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#creating a database object
db = SQLAlchemy(app)

#i will store the data from the browser into a file locally
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    description = db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.now())


    def __repr__(self):
        return f"<Todo {self.id}> - {self.title}>"
# 
@app.route("/")
def hello_world():
    todo = Todo(title="Learn Flask", description="Learn Flask", date_created=datetime.now())
    db.session.add(todo)
    db.session.commit()
    return render_template("hello.html")    #render_template is a function that takes a template name and returns the rendered html
#defining another endpoint
@app.route("/show")
def show():
    all_todo= Todo.query.all()
    return "show" 
@app.route("/bye")
def bye():
    return "bye"

if __name__ == "__main__":
    app.run(debug=True, port=2000)
