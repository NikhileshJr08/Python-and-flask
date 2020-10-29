import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    #Setting up a relationship between puppy and toy
    #One to many relationship meaning one dog can have many toys
    toys = db.relationship('toy',backref = 'puppy',lazy = 'dynamic')
    #Setting up a relationship between puppy and owner
    #One to one relationship meaning one dog is owned by only one owner
    owner = db.relationship('owner',backref = 'puppy',uselist = False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and the owner name is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner yet and is ready for adoption"

    def report_toys(self):
        print("Here is the list of my toys:")
        for toy in self.toys:
            print(toy.item_name)


class toy(db.Model):

    __tablename__ = 'toys'

    id = db.Column(db.Integer,primary_key = True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,item_name,puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id

class owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id
