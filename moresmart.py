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

@app.route('/post_test/', methods=['POST'])
def add_entry():
	input_text = request.get_data().decode("utf-8") 
	print("DATA", input_text)
	if not isinstance(input_text, str):
		print('bad')	
		return "bad"

	#g.db.execute('insert into notes (text) values (?)', [input_text])
	#g.db.commit()
	#flash('New entry was successfully posted')
	#return redirect(url_for('root'))
	return "good"

@app.route('/search/<string:query>/', methods=['GET'])
def search(query):
	print(query)	
	return json.dumps({'response': query})

if __name__ == "__main__":
    app.run(debug=True)

