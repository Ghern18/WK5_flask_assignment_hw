from flask_smorest import Blueprint

bp = Blueprint('students', __name__, description="Assignments for Students")

from . import routes