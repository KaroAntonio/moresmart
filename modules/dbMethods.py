# Python module for database functions.
import json
import ast

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

#Wrapper, String to JSON
def toJSON(string):
    return json.loads(string)

#wrapper, json to string
def toString(JSON):
    return json.dumps(JSON)


#returns all courses as a dict, pass in the query
def returnAllCourses(courses):
    dict = {"school":[], "department":[],"course":[]}
    for item in courses:
        dict["school"].append(item.school)
        dict["department"].append(item.department)
        dict["course"].append(item.course)

        #Sorts dict
        dict["schools"] = dict["schools"].sort()
        dict["deparment"] = dict["department"].sort()
        dict["course"] = dict["course"].sort()
    return json.dumps(dict)

#conditions should be a dict, no arrays inside, returns result.
def queryCourse(query):
    # structure of query might change
    #right  now ,we treat query as a json/dict
    school = query["school"]
    course = query["course"]

    result = db.session.query(Subject).filter(Subject.course == course, Subject.school == school)
    return result
#we need to process query after we receieve, and after we get id

#query should be a dict containing price and id, no arrays, again.
def queryTutor(query):
    id = query["id"]
    minprice = query["minprice"]
    maxprice = query["maxprice"]
    result = db.session.query(User).filter(User.pricemin <= maxprice)
    finalResult = []
    for item in result:
        subjects = item.subjects
        subjectsDict = ast.literal_eval(subjects)
        print (subjectsDict)
        courses = subjectsDict["subjects"]
        for i in courses:
            if str(i) ==  str(id):
                finalResult.append(item)
    return finalResult
