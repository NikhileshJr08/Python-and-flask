#This .py file contains the form code

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField

class AddForm(FlaskForm):

    name = StringField("Name of the Puppy:")
    breed = StringField("Breed of the Puppy:")
    age = StringField("Age of the Puppy:")
    submit = SubmitField('Add the Puppy')


class DelForm(FlaskForm):

    id = IntegerField("ID number of the Puppy to remove:")
    submit = SubmitField("Remove Puppy")

class OwnerForm(FlaskForm):

    name = StringField("Name of the owner:")
    puppy_id = IntegerField("ID of the dog:")
    submit = SubmitField("Submit to add owner")
