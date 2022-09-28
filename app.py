from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    description = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default=False)


@app.route("/")
def index():
    todo_list = Todo.query.filter_by(complete=False).all()
    return render_template("index.html", todos=todo_list)


@app.route("/todo")
def todo():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template("todo.html", todos=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    description = request.form.get("description")
    new_todo = Todo(title=title, description=description)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("todo"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    updated_todo = Todo.query.filter_by(id=todo_id).first()
    updated_todo.complete = not updated_todo.complete
    db.session.commit()
    return redirect(url_for("todo"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    deleted_todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(deleted_todo)
    db.session.commit()
    return redirect(url_for("todo"))


if __name__ == "__main__":
    # db.create_all()
    # new_todo = Todo(title="Todo 4", description="hello world", complete=False)
    # db.session.add(new_todo)
    # db.session.commit()
    app.run(debug=True)
