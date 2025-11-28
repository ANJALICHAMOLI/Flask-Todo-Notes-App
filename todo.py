from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TODO.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

UPLOAD_FOLDER = os.path.join("static", "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=True)
    pdf_filename = db.Column(db.String(300), nullable=True)  # store uploaded PDF filename
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/add_subtask/<int:sno>", methods=["POST"])
def add_subtask(sno):
    todo = Todo.query.get_or_404(sno)
    title = request.form['subtask_title']
    subtask = SubTask(todo_id=todo.sno, title=title, completed=False)
    # reset parent to incomplete if it was completed
    todo.completed = False
    db.session.add(subtask)
    db.session.commit()
    return redirect(url_for("homepage"))
# ✅ Added SubTask model here
class SubTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_id = db.Column(db.Integer, db.ForeignKey("todo.sno"), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)
    # auto update from subtasks
    subtasks = db.relationship(
        "SubTask",
        backref="todo",
        lazy=True,
        cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    
@app.route("/notes", methods=["GET", "POST"])
def notes():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form.get("content")
        pdf_file = request.files.get("pdf_file")
        pdf_filename = None
        if pdf_file and pdf_file.filename != "":
            pdf_filename = secure_filename(pdf_file.filename)
            pdf_file.save(os.path.join(app.config["UPLOAD_FOLDER"], pdf_filename))
        note = Note(title=title, content=content, pdf_filename=pdf_filename)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for("notes"))
    # only ONE query + ONE return
    all_notes = Note.query.order_by(Note.date_created.desc()).all()
    all_reminders = Reminder.query.order_by(Reminder.date_created.desc()).all()
    return render_template("notes.html", notes=all_notes, reminders=all_reminders)  
    
@app.route("/toggle_subtask/<int:id>", methods=["POST"])
def toggle_subtask(id):
    subtask = SubTask.query.get_or_404(id)
    subtask.completed = not subtask.completed 
     # check parent status: completed only if ALL subtasks are completed
    parent = subtask.todo
    parent.completed = all(st.completed for st in parent.subtasks)
    db.session.commit()
    return redirect(url_for("homepage"))         


@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        

if __name__ == "__main__":
    with app.app_context():
        # Drop all existing tables (useful during development)
        db.drop_all()
        # Create tables again with updated schema
        db.create_all()
    app.run(debug=True, port=8000)