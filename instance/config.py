import os
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'
SQLALCHEMY_DATABASE_URI="sqlite:///{}".format(os.path.join(basedir, "database.db"))
