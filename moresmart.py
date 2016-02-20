import json
from flask import Flask, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

#CONFIG
#http://killtheyak.com/use-postgresql-with-django-flask/
#DATABASE = 'static/fuzzywuzzy.db'
DEBUG = True
SQLALCHEMY_DATABASE_URI = "postgresql://yourusername:yourpassword@localhost/yournewdb"

# create eur little application :)
app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)
db = SQLAlchemy(app)

@app.route('/')
def root():
	#return "Hello"
    	return app.send_static_file('index.html')

@app.route('/post_test', methods = ['POST'])
def post_test():
    input_json = request.get_json(force=True)
    return jsonify('success')  # back to a string to produce a proper response

@app.route('/search/<string:query>/', methods=['GET'])
def search(query):
	print(query)	
	return json.dumps({'response': query})

if __name__ == "__main__":
    app.run(debug=True)

