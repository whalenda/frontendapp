#! /usr/bin/env python2.7

import requests
import unittest

class TestAccountInterface(unittest.TestCase):
    def setup(self):
        self.sortTestMethodsUsing = None

    def test0_create_account(self):
        URL = "http://localhost:8000/accounts/create"
        data = {
            'email': 'email1@test.com',
            'password': 'password1234',
            'confirm': 'password1234'
        }
        response = requests.post(URL, data=data)
        self.assertTrue(response.status_code == 201, "Basic Account Creation does not work.")

        del data['email']
        response = requests.post(URL, data=data)
        self.assertTrue(response.status_code == 400, "KeyError should have raised 400")

        data['email'] = 'email1@test.com'
        del data['password']
        response = requests.post(URL, data=data)
        self.assertTrue(response.status_code == 400, "KeyError should have raised 400")

        data['password'] = "password1234"
        del data['confirm']
        response = requests.post(URL, data=data)
        self.assertTrue(response.status_code == 400, "KeyError should have raised 400")

        data = {
            'email': '@test.com',
            'password': 'password1234',
            'confirm': 'password1234'
        }
        response = requests.post(URL, data=data)
        self.assertTrue(response.status_code == 403, "Email Validation for local-part does not work.")

        data = {
            'email': 'me@@test.com',
            'password': 'password',
            'confirm': 'password'
        }
        response = requests.post(URL, data=data)
        self.assertTrue(response.status_code == 403, "Email Validation for multiple @'s does not work.")

        data = {
            'email': 'me@invalid',
            'password': 'password',
            'confirm': 'password'
        }
        response = requests.post(URL, data=data)
        self.assertTrue(response.status_code == 403, "Email Validation for '.' in the domain does not work.")

        data = {
            'email': 'email1@test.com',
            'password': 'otherpassword',
            'confirm': 'otherpassword'
        }
        response = requests.post(URL, data=data)
        self.assertTrue(response.status_code == 403, "Duplicate Emails should not be allowed.")

        data = {
            'email': 'me@umich.edu',
            'password': 'mypassword',
            'confirm': 'nottherightpassword'
        }
        response = requests.post(URL, data=data)
        self.assertTrue(response.status_code == 403, "Passwords should match.")

        data = {
            'email': 'me@umich.edu',
            'password': 'short',
            'confirm': 'short'
        }
        response = requests.post(URL, data=data)
        self.assertTrue(response.status_code == 403, "Passwords should be at least 8 characters.")


    def test1_login(self):
        URL = "http://localhost:8000/accounts/login"
        data = {
            'email': "email1@test.com",
            'password': "password1234"
        }
        response = requests.post(URL, data=data)
        self.assertTrue(response.status_code == 200, "Basic login does not work")


    def test2_delete_account(self):
        URL = "http://localhost:8000/accounts/delete"
        data = {
            'email': "email1@test.com",
            'password': "password1234"
        }
        response = requests.post(URL, data=data)
        self.assertTrue(response.status_code == 204, "Basic Account Deletion does not work.")
