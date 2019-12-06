# demonstrate basic use of flask

from flask import Flask

# create a new Flask app instance
app = Flask(__name__)

# create the first route by defining the starting point, or 'root'
@app.route('/')
def hello_world():
	return 'Hello world'

'''
TO RUN:
execute export FLASK_APP='name of program.py'
flask run
'''