from flask import Flask
from flask_smorest import Api
from Config import Config


app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)


from resources.student import bp as student_bp
api.register_blueprint(student_bp)

from resources.spell import bp as spell_bp
api.register_blueprint(spell_bp)