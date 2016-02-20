import json
from flask import Flask, request, url_for

# configuration
#DATABASE = 'static/fuzzywuzzy.db'
DEBUG = True

# create eur little application :)
app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)


@app.route('/')
def root():
	#return "Hello"
    	return app.send_static_file('index.html')

@app.route('/post_test', methods = ['POST'])
def post_test():
    input_json = request.get_json(force=True)
    return jsonify()  # back to a string to produce a proper response

@app.route('/search/<string:query>/', methods=['GET'])
def search(query):
    notes = [
        NoteMatch('There there.'),
        NoteMatch('Where?'),
        NoteMatch('ttt'),
    ]

    matches = [i for i in notes if i.findMatches(query)]
    return json.dumps({'matches': noteMatchesToJson(matches)})

if __name__ == "__main__":
    app.run(debug=True)

