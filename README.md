# MyHero Data Service

This is the Data Service for a basic microservice demo application.
This provides a data storage layer for a voting system where users can vote for their favorite movie superhero.

Details on deploying the entire demo to a Mantl cluster can be found at
* MyHero Demo - [hpreston/myhero_demo](https://github.com/hpreston/myhero_demo)

The application was designed to provide a simple demo for Cisco Mantl.  It is written as a simple Python Flask application and deployed as a docker container.

Other services are:
* Data - [hpreston/myhero_data](https://github.com/hpreston/myhero_data)
* App - [hpreston/myhero_app](https://github.com/hpreston/myhero_app)
* Web - [hpreston/myhero_web](https://github.com/hpreston/myhero_web)

The docker containers are available at
* Data - [hpreston/myhero_data](https://hub.docker.com/r/hpreston/myhero_data)
* App - [hpreston/myhero_web](https://hub.docker.com/r/hpreston/myhero_app)
* Web - [hpreston/myhero_web](https://hub.docker.com/r/hpreston/myhero_web)

## Basic Application Details

Required

* flask
* ArgumentParser

# Installation

    pip install -r requirements.txt

# Usage

    python myhero_data/myhero_data.py

# Accessing

Initial and Basic APIs
* Basic List of Hero Choices
  * `curl http://localhost:5000/hero_list`
* Current results calculations
  * `curl http://localhost:5000/results`
* Place a vote for an option
  * `curl http://localhost:5000/vote/<HERO>`

Additional APIs for Option Management
* Get the current list of options for voting
  * `curl -X GET http://localhost:5000/options`
* Add a new option to the list
  * `curl -X PUT http://localhost:5000/options -d '{"option":"Deadpool"}'`
* Replace the entire options list
  * `curl-X POST -H "key: New List" http://localhost:5000/options -d @sample_post.json`
  * Requires a Header 'key' to be sent with any value accepted
  * Data should be of same format as a GET request
* Delete a single option from the list
  * `curl -X DELETE -H "key: Delete" http://localhost:5000/options/Deadpool`
  * Requires a Header 'key' to be sent with any value accepted
