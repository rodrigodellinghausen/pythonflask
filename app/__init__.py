__author__ = 'Rodrigo WSW'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# ou
# app.config.from_object(config[config_name])
# ou
app.config.from_object('app.config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# aqui tem que registrar o blueprint
from .enpoints import rest as rest_blueprint
app.register_blueprint(rest_blueprint)


