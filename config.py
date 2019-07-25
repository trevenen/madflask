import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'Sm9obiBTY2hyb20ga2lja3MgYXNz')
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(basedir, "database.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://user:test@localhost/databasename"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = "postgresql://user:test@localhost/databasename"

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
