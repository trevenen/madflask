from flask import Flask
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    db.init_app(app)
    flask_bcrypt.init_app(app)
    

    # Load the default configuration
    app.config.from_object(config_by_name[config_name])

    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py')

    # Defining the upload object for the data 
    docs = UploadSet('datafiles', DOCUMENTS)

    # Defining the uploaded data file destination
    app.config['UPLOADED_DATAFILES_DEST'] = 'static/uploads'

    # Initialize the uplaod object in the app
    configure_uploads(app, docs)

    # Allow extentions 
    ALLOWED_EXTENSIONS = {'json'}
    #import blueprint
    from app.views.views import view_blueprint
    app.register_blueprint(view_blueprint)

    return app
