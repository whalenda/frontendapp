#! /usr/bin/env python2.7

import flask
import rest_api

from flask import request
from flask import jsonify

import bcrypt

def normalize_email(email):
    return email.strip().lower()

def valid_email(email):
    if len(email.split('@')) != 2:
        return False

    user, domain = email.split('@')

    if not user or len(user) > 64:
        return False

    if '.' not in domain:
        return False

    return True

# Account Interface
@rest_api.app.route("/accounts/create", methods=["POST"])
def create_account():
    # Validating Input
    try:
        email = request.form['email']
    except KeyError:
        return jsonify({'error': "'email' key was not found in form body"}), 400

    try:
        password = request.form['password']
    except KeyError:
        return jsonify({'error': "'password' key was not found in form body"}), 400

    try:
        confirm = request.form['confirm']
    except KeyError:
        return jsonify({'error': "'confirm' key was not found in form body"}), 400

    email = normalize_email(email)

    if not valid_email(email):
        return jsonify({'error': "This is an invalid email address."}), 403

    # Check to see if we saw this email before?
    cursor = rest_api.db.get_db().cursor()
    results = cursor.execute("SELECT * FROM Accounts WHERE email=:email",
                           {'email': email }).fetchone()
    if results:
        return jsonify({'error': "There is already an account associated with this email."}), 403

    # Make sure the passwords match
    if password != confirm:
        return jsonify({'error': "Passwords do not match"}), 403

    if not password or len(password) < 8:
        return jsonify({'error': "Passwords must be at least 8 characters"}), 403

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor.execute("INSERT INTO Accounts VALUES (?, ?)", (email, hashed_password))

    return jsonify({"message": "Account created successfully"}), 201


@rest_api.app.route("/accounts/login", methods=["POST"])
def login():
    # Validating input
    try:
        email = request.form['email']
    except KeyError:
        return jsonify({'error': "'email' key was not found in form body"}), 400

    try:
        password = request.form['password']
    except KeyError:
        return jsonify({'error': "'password' key was not found in form body"}), 400

    # Check if we have a user with email
    cursor = rest_api.db.get_db().cursor()
    results = cursor.execute("SELECT * FROM Accounts WHERE email=:email",
                           {'email': email }).fetchone()
    if results:
        hashed_password = results[1]

        # we located the user now compare passwords
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            return jsonify({'message': "Login successful."}), 200

    return jsonify({'error': "Invalid email or password"}), 401



@rest_api.app.route("/accounts/delete", methods=["POST"])
def delete_account():
    # Validating input
    try:
        email = request.form['email']
    except KeyError:
        return jsonify({'error': "'email' key was not found in form body"}), 400

    try:
        password = request.form['password']
    except KeyError:
        return jsonify({'error': "'password' key was not found in form body"}), 400

    # Check if we have a user with email
    cursor = rest_api.db.get_db().cursor()
    results = cursor.execute("SELECT * FROM Accounts WHERE email=:email",
                           {'email': email }).fetchone()
    if results:
        hashed_password = results[1]

        # we located the user now compare passwords
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            cursor.execute("DELETE FROM Accounts WHERE email=?", (email,))
            return jsonify({'message': "Delete successful."}), 204

    return jsonify({'error': "Invalid email or password"}), 401
