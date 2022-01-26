# Created By  : Galileo Garibaldi, Simón López
# Created Date: 25/01/2022 
# Modified Date: -
# version ='1.0'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('configuration.DevelopmentConfig')
db = SQLAlchemy(app)

from api3.tasks.view import enp1
from api3.student_api.api_student import category_view
app.register_blueprint(enp1)
db.create_all()