from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('configuration.DevelopmentConfig')
db = SQLAlchemy(app)

from api3.endpoints.view import enp1
app.register_blueprint(enp1)
db.create_all()
