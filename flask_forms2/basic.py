from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,RadioField,
                    SelectField,TextAreaField,SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

    breed = StringField("What breed are you?", validators = [DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField("What's your mood today?",choices = [('Happy','Happy'),('Excited','Excited')])
    fav_food = SelectField("What's your favourite food?",choices = [('Chicken','Chicken'),('Beef','Beef'),('Fish','Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/',methods = ['GET', 'POST'])
def index():

    form = InfoForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['fav_food'] = form.fav_food.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))

    return render_template('index.html',form = form)

@app.route('/thankyou')
def thankyou():

    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug = True)
