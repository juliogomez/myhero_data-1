# MyHero Data Service

This is the Data Service for a basic microservice demo application.
This provides a data storage layer for a voting system where users can vote for their favorite movie superhero.

Details on deploying the entire demo to a Kubernetes cluster can be found at

* DevOps tutorial - [juliogomez/devops](https://github.com/juliogomez/devops)

The application was designed to provide a simple demo for Kubernetes.  It is written as a simple Python Flask application and deployed as a docker container.

Other services are:

* Data - [hpreston/myhero_data](https://github.com/hpreston/myhero_data)
* App - [hpreston/myhero_app](https://github.com/hpreston/myhero_app)
* Web - [hpreston/myhero_web](https://github.com/hpreston/myhero_web)
* UI - [hpreston/myhero_ui](https://github.com/hpreston/myhero_ui)
* Ernst - [hpreston/myhero_ernst](https://github.com/hpreston/myhero_ernst)
  * Optional Service used along with an MQTT server when App is in "queue" mode
* Spark Bot - [hpreston/myhero_spark](https://github.com/hpreston/myhero_spark)
  * Optional Service that allows voting through IM/Chat with a Cisco Spark Bot
* Tropo App - [hpreston/myhero_tropo](https://github.com/hpreston/myhero_tropo)
  * Optional Service that allows voting through TXT/SMS messaging


The docker containers are available at

* Data - [hpreston/myhero_data](https://hub.docker.com/r/hpreston/myhero_data)
* App - [hpreston/myhero_app](https://hub.docker.com/r/hpreston/myhero_app)
* Web - [hpreston/myhero_web](https://hub.docker.com/r/hpreston/myhero_web)
* UI - [hpreston/myhero_ui](https://hub.docker.com/r/hpreston/myhero_ui)
* Ernst - [hpreston/myhero_ernst](https://hub.docker.com/r/hpreston/myhero_ernst)
  * Optional Service used along with an MQTT server when App is in "queue" mode
* Spark Bot - [hpreston/myhero_spark](https://hub.docker.com/r/hpreston/myhero_spark)
  * Optional Service that allows voting through IM/Chat with a Cisco Spark Bot
* Tropo App - [hpreston/myhero_tropo](https://hub.docker.com/r/hpreston/myhero_tropo)
  * Optional Service that allows voting through TXT/SMS messaging

## Basic Application Details

Required

* flask
* ArgumentParser
* requests

# Environment Installation

    pip install -r requirements.txt

# Basic Usage

In order to run, the service needs 1 piece of information to be provided:

* Data Server Authentication Key to Require

This detail can be provided in one of three ways.
* As a command line argument
  - `python myhero_data/myhero_data.py --datasecret "DATA AUTH KEY" `
* As environment variables
  - `export myhero_data_key="DATA AUTH KEY"`
  - `python myhero_data/myhero_data.py`
* As raw input when the application is run
  - `python myhero_data/myhero_data.py`
  - `Data Server Key: DATA AUTH KEY`

A command line argument overrides an environment variable, and raw input is only used if neither of the other two options provide needed details.


# Accessing

Initial and Basic APIs
These are v1 APIs that require no authentication and will eventually be removed

* Basic List of Hero Choices
  * `curl http://localhost:5000/hero_list`
* Current results calculations
  * `curl http://localhost:5000/results`
* Place a vote for an option
  * `curl http://localhost:5000/vote/<HERO>`

New v2 APIs
These newer APIs require authentication as well as support more features

* Get the current list of options for voting
  * `curl -X GET -H "key: DATA AUTH KEY" http://localhost:5000/options`
* Add a new option to the list
  * `curl -X PUT -H "key: DATA AUTH KEY" http://localhost:5000/options -d '{"option":"Deadpool"}'`
* Replace the entire options list
  * `curl-X POST -H "key: DATA AUTH KEY" http://localhost:5000/options -d @sample_post.json`
  * Data should be of same format as a GET request
* Delete a single option from the list
  * `curl -X DELETE -H "key: DATA AUTH KEY" http://localhost:5000/options/Deadpool`
* Place a Vote for an option
  * `curl -X POST -H "key: DATA AUTH KEY" http://localhost:5000/vote/Deadpool`
* Get current results
  * `curl -X GET -H "key: DATA AUTH KEY" http://localhost:5000/results`

# Local Development with Vagrant

I've included the configuration files needed to do local development with Vagrant in the repo.  Vagrant will still use Docker for local development and requires the following be installed on your laptop: 

* [Vagrant 2.0.1 or higher](https://www.vagrantup.com/downloads.html)
* [Docker](https://www.docker.com/community-edition)

To start local development run:

* `vagrant up`
*  Now you can interact with the API or interface at localhost:15000 (configured in Vagrantfile)
  - example:  from your local machine `curl -H "key: DevData" http://localhost:15000/options`
  - Environment Variables are configured in Vagrantfile for development

Each of the services in the application (i.e. myhero_web, myhero_app, and myhero_data) include Vagrant support to allow working locally on all three simultaneously.

# Local Development with docker-compose

I've included the configuration files needed to do local development with docker-compose in the repo.  docker-compose will still use Docker for local development and requires the following be installed on your laptop: 

* [Docker](https://www.docker.com/community-edition)

To start local development run:

* `docker-compose up`
*  Now you can interact with the API or interface at localhost:15000 (configured in docker-compose.yml)
  - example:  from your local machine `curl -H "key: DevData" http://localhost:15000/options`
  - Environment Variables are configured in .env for development

Each of the services in the application (i.e. myhero_web, myhero_app, and myhero_data) include docker-compose support to allow working locally on all three simultaneously.