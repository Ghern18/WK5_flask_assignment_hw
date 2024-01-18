#from app import app

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

#error showing from this line. 
    
    #tried downloading flask migrate again and restarting but still getting an unknown error
    #insomnia showing as not qorking 404, but it's running!
    