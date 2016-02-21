import json, os
from flask import Flask, request, url_for, jsonify,redirect
from flask.ext.login import LoginManager, UserMixin, login_user, login_required, current_user
from flask.ext.sqlalchemy import SQLAlchemy
from flask_oauth2_login import GoogleLogin
import requests
from twilio.rest import TwilioRestClient

#CONFIG
#http://killtheyak.com/use-postgresql-with-django-flask/
#DATABASE = 'static/fuzzywuzzy.db'
DEBUG = True
#http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

# create eur little application :)
app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
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
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    googleid = db.Column(db.String(64))
    lastname = db.Column(db.String(50))
    firstname = db.Column(db.String(50))
    contactinfo = db.Column(db.String(1024))
    stats = db.Column(db.String(5120))
    subjects = db.Column(db.String(1024))
    pricemin = db.Column(db.Integer)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, googleid, lastname, firstname, contactinfo, stats, subjects, pricemin, email, password):
        self.googleid = googleid
        self.lastname = lastname
        self.firstname = firstname
        self.contactinfo = contactinfo
        self.stats = stats
        self.subjects = subjects
        self.pricemin = pricemin
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email


# Subject Model
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String(64))
    department = db.Column(db.String(16))
    course = db.Column(db.String(64))

    def __init__(self, school, department, course):
        self.school = school
        self.department = department
        self.course = course
 

    def __repr__(self):
        return '<User %r>' % self.course

@app.route("/")
def index():
    return app.send_static_file('landing.html')

@login_manager.user_loader
def load_user(userid):
    return User.query.filter_by(id=userid).all()[0]

@google_login.login_success
def login_success(token, profile):
	print(profile)
	users = User.query.filter_by(googleid=profile['id']).all()
	if len(users) != 0:
		#login existing user
		login_user(users[0])
		return redirect("/request_page", code=302)
	else:
		#create new user to add
		user = User(profile['id'],profile['family_name'],profile['given_name'],"","","",0,profile['email'],"")
		db.session.add(user)
		db.session.commit()
		login_user(user)
		return redirect("/more_info", code=302)

@google_login.login_failure
def login_failure(e):
  return str(e)

@app.route('/more_info')
@login_required
def more_info():
	return app.send_static_file('more_info.html')

@app.route('/request_page')
@login_required
def request_page():
	return "Make a Request"

@app.route('/get_google/', methods=['GET'])
def get_google():
	return google_login.authorization_url()

@app.route('/request/<string:data>/', methods=['GET'])
@login_required
def request_data(data):
    #price, course details [school, course, subject]
    #{'price':123,'school':'plebs4lyfe','course':'asd','subject':'asd'}
	return data

@app.route('/post_test/', methods=['POST'])
@login_required
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

@app.route('/smooch-hook/', methods=['POST'])
def smooch_hook():
    data = request.get_data().decode("utf-8")
    print(data)
    text = json.loads(data)['messages'][0]['text']
    #check if author is validated, if no, compare text to validation key,
    #else check if it is  a request
    return text

def post_smooch(uid,text):
    url = 'https://api.smooch.io/v1/appusers/'+uid+'/conversation/messages'
    payload = {'text':text,'role':'appMaker'}
    headers = {'content-type':'application/json','authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IjU2YzkwZTAzOTMzYmNjMmEwMGU4ZTFkYSJ9.eyJzY29wZSI6ImFwcCJ9._CfWALWAilTQxyGlfeSpFR1xOvcUrDIxQV3yv08Xeo8'}
    r = requests.post(url, json=payload, headers=headers)
    return r

def post_twilio(num,text):
    # put your own credentials here 
    ACCOUNT_SID = "AC34a2bfb497e4a8f51be5b4396e89e327" 
    AUTH_TOKEN = "c4335ee027bf3a7de7a3a24ac59f0d9c" 

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

    client.messages.create(
        to=num, 
        from_="+14387937578", 
        body=text, 
    )

@app.route('/post_info/', methods=['POST'])
@login_required
def send_number_validation():
    input_text = request.get_data().decode("utf-8") 
    print("DATA", input_text)
    print(current_user)
    if not isinstance(input_text, str):
        print('bad')	
        return "bad"
    #USE SMOOCH TO TEXT TO NUMBER
    return "good"

@app.route('/search/<string:query>/', methods=['GET'])
@login_required
def search(query):
	print(query)	
	return json.dumps({'response': query})

if __name__ == "__main__":
    app.run(debug=True)

