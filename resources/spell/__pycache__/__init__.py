from flask_smorest import Blueprint

bp = Blueprint ('spells', __name__, description='Ops on Spells', url_prefix='/spell')

from . import routes