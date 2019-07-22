import os
from flask import Flask
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from config import config_by_name, Config
from flask_bootstrap import Bootstrap

flask_bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/static/uploads'


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    flask_bcrypt.init_app(app)
    # setting login manager
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    Bootstrap(app)
    migrate = Migrate(app, db)
    # Define the database file enviromental variable
    # Load the default configuration
    #app.config.from_object(config_by_name[config_name])
    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py')
    # Defining the upload object for the data 
    # docs = UploadSet('datafiles', DOCUMENTS)
    # # Defining the uploaded data file destination
    app.config['UPLOADED_DATAFILES_DEST'] = UPLOAD_FOLDER
    # # Initialize the uplaod object in the app
    # configure_uploads(app, docs)
    # Allow extentions 
    #app.config["ALLOWED_EXTENSIONS"] = ALLOWED_EXTENSIONS
    #import blueprint
    from .views.views import view_blueprint
    app.register_blueprint(view_blueprint)
    return app
