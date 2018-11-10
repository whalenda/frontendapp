#! /usr/bin/env python2.7

import flask

app = flask.Flask(__name__)

app.config.from_object("rest_api.config")

import rest_api.api
import rest_api.db
