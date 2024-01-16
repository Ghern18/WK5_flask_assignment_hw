from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config


app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.student_model import StudentModel
from models.spell_model import SpellModel

from resources.student import bp as student_bp
api.register_blueprint(student_bp)

from resources.spell import bp as spell_bp
api.register_blueprint(spell_bp)