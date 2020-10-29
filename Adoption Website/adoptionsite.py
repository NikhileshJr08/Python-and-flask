#Main .py file for adoption website
import os
from forms import AddForm,DelForm,OwnerForm
from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

##########################################
############ Database Section ############
##########################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

##################
##### Models #####
##################

class puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    breed = db.Column(db.Text)
    age = db.Column(db.Integer)

    owner = db.relationship('owner',backref = 'puppy', uselist = False)

    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} of {self.breed} type and he/she is {self.age} years old whose ID is {self.id} and owner name is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} of {self.breed} type and he/she is {self.age} years old whose ID is {self.id} and does not have an owner"

class owner(db.Model):

    __tablename__ = 'owner'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner name is {self.name}"


######################
### View Functions ###
######################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add',methods=['GET','POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data
        breed = form.breed.data
        age = form.age.data

        new_pup = puppy(name,breed,age)

        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('owner_pup'))

    return render_template('add.html',form = form)

@app.route('/delete',methods=['GET','POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data
        pup = puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('delete.html',form = form)

@app.route('/list')
def list_pup():
    all_puppies = puppy.query.all()
    return render_template('list.html',all_puppies = all_puppies)

@app.route('/owner',methods = ['GET','POST'])
def owner_pup():

    form = OwnerForm()

    if form.validate_on_submit():

        name = form.name.data
        puppy_id = form.puppy_id.data

        new_owner = owner(name,puppy_id)

        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('owner.html',form = form)

if __name__ == '__main__':
    app.run(debug=True)
