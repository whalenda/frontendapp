#! /usr/bin/env python2.7

import flask
import sqlite3
import config
import rest_api

def get_db():
    """Open a new database connection."""
    if not hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db = sqlite3.connect(config.DATABASE_FILENAME)
        flask.g.sqlite_db.execute("PRAGMA foreign_keys = ON")

    return flask.g.sqlite_db


@rest_api.app.teardown_appcontext
def close_db(error):
    if hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db.commit()
        flask.g.sqlite_db.close()
