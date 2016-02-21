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


def queryResponse(query_classes):
    parsed_query_classes = ast.literal_eval(query_classes)
    query_id = queryCourse(parsed_query_classes)[0].id
    price = parsed_query_classes["price"]
    
    query_tutor = {"id":query_id,"maxprice":price}
    return queryTutor(query_tutor)

#conditions should be a dict, no arrays inside, returns result.
def queryCourse(query):
    # structure of query might change
     #right  now ,we treat query as a json/dict
    school = query['school']
    course = query['course']

    result = db.session.query(Subject).filter(Subject.course == course, Subject.school == school)
    return result
#we need to process query after we receieve, and after we get id


#query should be a dict containing price and id, no arrays, again.
def queryTutor(query):
    id = query["id"]
    maxprice = query["maxprice"]
    result = db.session.query(User).filter(User.pricemin <= maxprice)
    finalResult = []
    for item in result:
        subjects = item.subjects
        subjectsDict = ast.literal_eval(subjects)
        courses = subjectsDict["subjects"]
        for i in courses:
            if str(i) ==  str(id):
                finalResult.append(item)
    return finalResult

def userAdditional(user, additional_info):
    email = user.email
    parsed_additional_info = ast.literal_eval(additional_info)
    user = User.query.filter_by(email == str(email))
    user.pricemin = int(additional_info["price"])
    user.subjects = str(parsed_additional_info["subjects"])
    user.contactinfo = str(parsed_additional_info["phone"])
    #user.smooch = str(parsed_additional_info["smooch"])
    db.session.commit()
