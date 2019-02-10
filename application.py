#!flask/bin/python
from flask import Flask, jsonify
from flask import request
import translate_utils as tu


application = Flask(__name__)	

# text = 'Hello, world!'
# target = 'ru'
location = '/Users/karansingh/Documents/Hack/My First Project-b7b011a569ea.json'

@application.route('/', methods = ['GET','POST'])
def index():
	text = request.args.get('text')
	return tu.translate_language(text, location)

if __name__ == '__main__':
    application.run(debug=True)


