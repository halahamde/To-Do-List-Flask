
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
#from markupsafe import re
from sqlalchemy_utils.types.choice import ChoiceType
import datetime
import json

from todo_forms import RegisrationForm, LoginForm , AddTaskForm , UpdateTaskForm , DeleteTaskForm


app = Flask(__name__)   # __main__
app.config['SECRET_KEY'] = "secret1234"


'''users = [
    {"name": "Ali", "email": "test@example.com", "password": "1234"},
    {"name": "Ahmed", "email": "test@example.com", "password": "1234"},
    {"name": "Test", "email": "test@example.com", "password": "1234"},
    ]
'''
tasks = [
    {"id": 1,"title": 'python', "description": "oop", "status": "in progress"},
    {"id": 2,"title": 'java', "description": "test@example.com", "status": "completed"},
    {"id": 3,"title": 'odoo', "description": "test@example.com", "status": "in progress"},
    ]


DATABASE_URI = "sqlite:///users.db"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db = SQLAlchemy(app)

'''USERS_TYPES = [
    ('admin', 'Admin'),
    ('user', 'User')
]'''

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    

class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f"Task('{self.title}', '{self.status}')"

@app.route('/', methods=['POST', 'GET'])
@app.route('/home')
def home():
    return render_template('basicnav.html')

@app.route('/tasks')
def get_tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        #user_data = request.form
        id = request.form["id"]
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
       
        new_user = User(username=username, email=email, id=id, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return 'There was an error while adding the user'
        
    else:
        return render_template('register.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    users = User.query.all()
    if request.method == 'POST':
        password = request.form["password"]
        email = request.form["email"]
        for user in users:
            if user.email == email and user.password == password:
                return redirect(url_for('get_tasks'))

    return render_template('login.html')

@app.route('/add', methods=['GET', 'POST'])
def addtask():
    if request.method == 'POST':
        id = request.form["id"]
        title = request.form["title"]
        description = request.form["description"]
        status = request.form["status"]
        new_task = Task(id=id, title=title, description=description, status=status)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('get_tasks'))
        except:
            return 'There was an error while adding the task'
    else:
         return render_template('addTask.html')

@app.route('/update', methods=['GET', 'POST'])
def updatetask():
    if request.method == 'POST':
        
        id = request.form["id"]
        task = Task.query.get(id)
        task.id = id
        task.title = request.form["title"]
        task.description = request.form["description"]
        task.status = request.form["status"]
        try:
            db.session.commit()
            return redirect(url_for('get_tasks'))
        except:
            return 'There was an error while updating the task'
    return render_template('updateTask.html')

@app.route('/delete', methods=['GET', 'POST'])
def deletetask():
    if request.method == 'POST':
        id = request.form["id"]
        task = Task.query.filter_by(id=id).first()
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('get_tasks'))
    return render_template('deleteTask.html')
    
db.create_all()
app.run(debug=True)
