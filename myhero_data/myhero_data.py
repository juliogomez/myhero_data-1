#! /usr/bin/python
'''
    Data Service for Simple Superhero Voting Application

    This is the Data Service for a basic microservice demo application.
    The application was designed to provide a simple demo for Cisco Mantl

'''
__author__ = 'hapresto'

from flask import Flask, make_response, request, jsonify, Response
import datetime, json
from collections import Counter

app = Flask(__name__)
data_file = "heros.txt"

@app.route("/hero_list")
def hero_list():
    hero_list = []
    with open("heros.txt") as f:
        for line in f:
            line = line.rstrip()
            hero_list.append(line)
    resp = make_response(jsonify(heros=hero_list))
    return resp

@app.route("/vote/<hero>")
def vote(hero):
    with open("votes.txt", "a") as f:
        f.write(hero + "\n")
    resp = make_response(jsonify(result="1"))
    return resp

@app.route("/results")
def results():
    tally = Counter()
    with open("votes.txt") as f:
        for line in f:
            line = line.rstrip()
            tally[line] += 1
    resp = make_response(jsonify(tally))
    return resp

@app.route("/options", methods=["GET", "PUT", "POST"])
def options_route():
    '''
    Methods used to view options, add new option, and replace options.
    '''
    if request.method == "GET":
        options = {"options":option_list()}
        status = 200
    if request.method == "PUT":
        try:
            data = request.get_json(force=True)
            # Verify data is of good format
            # { "option" : "Deadpool" }
            options = {"options": add_option(data["option"])}
            status = 201
        except KeyError:
            error = {"Error":"API expects dictionary object with single element and key of 'option'"}
            status = 400
            resp = Response(json.dumps(error), content_type='application/json', status = status)
            return resp
    if request.method == "POST":
        # Simple authorization/verification
        # Require key to be sent in header
        headers = request.headers
        try:
            print("POST request key: " + headers["key"])
        except :
            error = {"Error": "Method requires authorization key."}
            print error
            status = 400
            resp = Response(json.dumps(error), content_type='application/json', status=status)
            return resp
        try:
            data = request.get_json(force=True)
            # Verify that data is of good format
            # {
            # "options": [
            #     "Spider-Man",
            #     "Captain America",
            #     "Batman",
            #     "Robin",
            #     "Superman",
            #     "Hulk",
            #     "Thor",
            #     "Green Lantern",
            #     "Star Lord",
            #     "Ironman"
            # ]
            # }
            print("New Options:")
            print(data["options"])
            options = {"options":replace_options(data["options"])}
            status = 201

        except KeyError:
            error = {"Error": "API expects dictionary object with single element with key 'option' and value a list of options"}
            status = 400
            resp = Response(json.dumps(error), content_type='application/json', status=status)
            return resp

    resp = Response(
        json.dumps(options, sort_keys=True, indent = 4, separators = (',', ': ')),
        content_type='application/json',
        status=status)
    return resp

@app.route("/options/<option>", methods=["DELETE"])
def option_delete_route(option):
    '''
    Delete an option from the the option_list.
    '''
    if request.method == "DELETE":
        # Simple authorization/verification
        # Require key to be sent in header
        headers = request.headers
        try:
            print("Delete request key: " + headers["key"])
        except :
            error = {"Error": "Method requires authorization key."}
            print error
            status = 400
            resp = Response(json.dumps(error), content_type='application/json', status=status)
            return resp

        options = {"options": remove_option(option)}
        status = 202
        resp = Response(
            json.dumps(options, sort_keys=True, indent=4, separators=(',', ': ')),
            content_type='application/json',
            status=status)
        return resp
    else:
        error = {"Error": "Route only acceptes a DELETE method"}
        status = 400
        resp = Response(json.dumps(error), content_type='application/json', status=status)
        return resp


def option_list():
    '''
    Get a list of possible options.
    '''
    options = []
    with open(data_file) as f:
        for line in f:
            line = line.rstrip()
            options.append(line)
    return options

def add_option(option):
    '''
    Add a new option to the list.
    '''
    options = option_list()
    if option.upper() in [o.upper() for o in options]:
        return "Option already in list."

    with open(data_file, "a") as f:
        f.write(option + "\n")

    return option_list()

def remove_option(option):
    '''
    Remove and option from the list.
    '''
    options = option_list()
    if option.upper() in [o.upper() for o in options]:
        options.remove(option)
        with open(data_file, "w") as f:
            f.write("\n".join(options) + "\n")
    return option_list()

def replace_options(options):
    '''
    Full replacement of option list
    '''
    with open(data_file, "w") as f:
        f.write("\n".join(options) + "\n")

    return option_list()

if __name__=='__main__':


    app.run(debug=True, host='0.0.0.0', port=int("5000"))

