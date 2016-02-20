import json, os
from flask import Flask, request, url_for, jsonify
from flask.ext.login import LoginManager, UserMixin
from flask.ext.sqlalchemy import SQLAlchemy
from flask_oauth2_login import GoogleLogin

#CONFIG
#http://killtheyak.com/use-postgresql-with-django-flask/
#DATABASE = 'static/fuzzywuzzy.db'
DEBUG = True
#http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

# create eur little application :)
app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)
db = SQLAlchemy(app)
app.config.update(
		  SECRET_KEY="secret",
		    GOOGLE_LOGIN_REDIRECT_SCHEME="http",
		    )
app.config.update(
		GOOGLE_LOGIN_REDIRECT_URIS='http://localhost:5000/login/google',
		GOOGLE_LOGIN_CLIENT_ID='250698810056-6b02gvftla1ek0j0p343fdkrnn1l6afl.apps.googleusercontent.com',
		GOOGLE_LOGIN_CLIENT_SECRET='LkuC7lG8mVIsgQrzrDTDGVDC',
)


google_login = GoogleLogin(app)

#User Model
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    googleid = db.Column(db.String(64))
    lastname = db.Column(db.String(50))
    firstname = db.Column(db.String(50))
    contactinfo = db.Column(db.String(1024))
    subjects = db.Column(db.String(1024))
    pricemin = db.Column(db.Integer)
    pricemax = db.Column(db.Integer)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, googleid, lastname, firstname, contactinfo, subjects, pricemin, pricemax, email, password):
        self.googleid = googleid
        self.lastname = lastname
        self.firstname = firstname
        self.contactinfo = contactinfo
        self.subjects = subjects
        self.pricemin = pricemin
        self.pricemax = pricemax
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email


# Subject Model
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String(64))
    course = db.Column(db.String(64))
    subject = db.Column(db.String(64))

    def __init__(self, school, course, subject):
        self.school = school
        self.course = course
        self.subject = subject

    def __repr__(self):
        return '<User %r>' % self.course


@app.route("/")
def index():
  return """
<html>
<a href="{}">Login with Google</a>
""".format(google_login.authorization_url())

@google_login.login_success
def login_success(token, profile):
	print(profile)
	return jsonify(token=token, profile=profile)

  #return (token,profile)

@google_login.login_failure
def login_failure(e):
  return str(e)

'''
@app.route('/')
def root():
	#return "Hello"
    	return app.send_static_file('index.html')
    	'''

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

