from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/todo")
def todo():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template("todo.html", todos=todo_list)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    description = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default=False)


if __name__ == "__main__":
    # db.create_all()
    # new_todo = Todo(title="Todo 4", description="hello world", complete=False)
    # db.session.add(new_todo)
    # db.session.commit()
    app.run(debug=True)
