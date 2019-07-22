import json, os
import plotly
import pandas as pd
from app import db
import plotly.graph_objects as go 
from app.utils.json_paser import Parser
from app.views.datachart import create_graph
from flask import Flask, render_template, send_file, request, redirect, url_for, flash, Blueprint, current_app as app
from flask_login import login_required, login_user, logout_user
from werkzeug.utils import secure_filename
from app.forms.forms import LoginForm, RegistrationForm, UploadForm
from app.models.models import User
from config import Config

view_blueprint = Blueprint('view', __name__)
ALLOWED_EXTENSIONS = {'json','csv'}

@view_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an user to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            password=form.password.data)

        # add user to the database
        db.session.add(user)
        db.session.commit()
        flash('You have successfully Create a user! You may now login.')
        # redirect to the login page
        return redirect(url_for('view.dashboard'))
    # load registration template
    return render_template('registration.html', form=form, title='Register')


@view_blueprint.route('/', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an user in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether user exists in the database and whether
        # the password entered matches the password in the database
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(
                form.password.data):
            # log user in
            login_user(user)

            if user.is_admin:
                return redirect(url_for('view.dashboard'))
            else:
                return redirect(url_for('view.dashboard'))
        # when login details are incorrect
        else:
            flash('Invalid email or password.')
    # load login template
    return render_template('index.html', form=form, title='Login')


@view_blueprint.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an user out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')
    # redirect to the login page
    return redirect(url_for('view.login'))



# Return true if the file type is json, csv, ... and false if not
def allowed_file(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)\
        [1].lower() in ALLOWED_EXTENSIONS

#Return file type
def file_type(file_name):
    return file_name.rsplit('.', 1)[1]

# Upload and parse data for the graph.
@view_blueprint.route('/upload', methods=['POST', 'GET'])
def upload_file():
    result = []
    form = UploadForm()
    if form.validate_on_submit():
        file  = form.file.data
        if not file:
            print('No file attached in request')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        # key_data = request.get['json_key']
        # key_data = key_data.split()
        if allowed_file(filename):
            file.save(os.path.join(app.config['UPLOADED_DATAFILES_DEST'], filename))
            f_type = file_type(filename)
            if f_type == 'json':
                try:
                    f = open(file, 'r')
                    json_obj = json.load(f)
                    res = Parser.parse_data(json_obj, key_data)
                    result.append(res)
                    f.close()
                except IOError:
                    print ('parameters error')
            elif f_type == 'csv':
                result = pd.read_csv(file)
                print(result)
            JsonData = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)
            return JsonData
    return render_template('upload_file.html', form=form, title='upload_file')

@view_blueprint.route('/dashboard')
def dashboard():
    pie = create_graph()
    return render_template('dashboard.html', graph_value=pie)
    