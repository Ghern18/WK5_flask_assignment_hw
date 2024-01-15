from flask_smorest import Blueprint

bp = Blueprint('student', __name__, description="Assignments for Students")

from . import routes