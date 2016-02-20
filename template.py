import json
from flask import Flask, request, url_for

import backend.search

# configuration
DATABASE = 'static/fuzzywuzzy.db'
DEBUG = True

# create eur little application :)
app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)

class NoteMatch:
    def __init__(self, text):
        self.text = text
        self.lowerText = text.lower()
        self.matchRanges = []

    def _addMatchRange(self, start, end):
        self.matchRanges.append((start, end))

    def findMatches(self, query):
        '''
        print(query)
        print(self.text)
        print(backend.search.search(query, self.text))
        '''
        for matchWord, index in backend.search.search(query, self.text):
            self._addMatchRange(index, index + len(matchWord))

        return len(self.matchRanges) > 0

def noteMatchesToJson(matches):
    return [{
        'text': i.text,
        'matchRanges': [
            {
                'start': m[0],
                'end':   m[1],
            } for m in i.matchRanges
        ],
    } for i in matches ]

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/tests/endpoint', methods=['POST'])
def get_bot_mission():
    input_json = request.get_json(force=True)
    print ('data from client:', input_json)
    return jsonify({'answer':42})

@app.route('/post_test', methods = ['POST'])
def getPersonById():
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

