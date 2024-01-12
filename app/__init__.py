from flask import Flask


app = Flask(__name__)


from resources.spell import routes
from resources.student import routes