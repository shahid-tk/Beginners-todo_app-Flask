import os
from datetime import datetime 
from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response 
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import parse_qs

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(300), nullable=False)
    done = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime, default=datetime.now)

@app.route('/update' , methods=['POST'])
def update():
    req = parse_qs(request.get_data().decode("utf-8"))
    id = int(req['id'][0])
    done = True if req['done'][0] == 'true' else False
    print(id, done)
    updateDone = Todo.query.filter_by(id=int(id)).first()
    updateDone.done = done
    db.session.commit()
    print(updateDone)
    return "OK"
   

@app.route('/delete/<id>')
def delete(id):
    todata = Todo.query.get(id)
    db.session.delete(todata)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/')
def home():
    tododata = Todo.query.all()
    return render_template('index.html', tododata=tododata)

@app.route('/add', methods=["POST"])
def add():
    dbtodo = Todo(todo=request.form['todoitems'], done=False)
    db.session.add(dbtodo)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)