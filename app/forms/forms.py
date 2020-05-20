import os
from flask import current_app as app
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import PasswordField, StringField, SubmitField, ValidationError, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

from app.models.models import User

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')

class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class UploadForm(FlaskForm):
    """
    Form for user to upload data
    """
    file = FileField('File', validators=[FileRequired()])
    submit = SubmitField('Upload')

""" class DataForm(FlaskForm):
    
    data =[]
    entries= os.listdir('app/static/uploads')
    i = 1
    for entry in entries:
        data.append([i, entry])
        i =i+1
    print(data)
    filename= SelectField('File name',choices = data, id='select_table', validators = [DataRequired()])
    #keydata = StringField('Key data', validators = [DataRequired()])
   # graph_type = StringField('Graph type', validators = [DataRequired()])
    submit = SubmitField('Submit') """