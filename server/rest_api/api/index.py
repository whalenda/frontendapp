#! /usr/bin/env python2.7

import flask
import rest_api

@rest_api.app.route("/", methods=["GET"])
def show_index():
    cursor = rest_api.db.get_db().cursor()
    #
    # for account in cursor.execute('SELECT * FROM noTable'):
    #     print(account)

    return "Welcome, to the Gulo Gulo rest API!"
