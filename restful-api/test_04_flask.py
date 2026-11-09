#!/usr/bin/python3

import unittest
import requests
import json
import time
import subprocess


BASE_URL = "http://127.0.0.1:5000"


class TestFlaskAPI(unittest.TestCase):

    def test_home(self):
        response = requests.get(BASE_URL + "/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Welcome to the Flask API!")

    def test_data_empty(self):
        response = requests.get(BASE_URL + "/data")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_add_user(self):
        user = {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }

        response = requests.post(
            BASE_URL + "/add_user",
            json=user
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["user"], user)

    def test_data_after_adding(self):
        response = requests.get(BASE_URL + "/data")
        self.assertEqual(response.status_code, 200)
        self.assertIn("john", response.json())

    def test_get_user(self):
        response = requests.get(BASE_URL + "/users/john")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json()["name"], "John")
        self.assertEqual(response.json()["age"], 30)

    def test_user_not_found(self):
        response = requests.get(BASE_URL + "/users/doesnotexist")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json(),
            {"error": "User not found"}
        )

    def test_status(self):
        response = requests.get(BASE_URL + "/status")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")

    def test_missing_username(self):
        response = requests.post(
            BASE_URL + "/add_user",
            json={"name": "Jane", "age": 28}
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"error": "Username is required"}
        )

    def test_duplicate_username(self):
        user = {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }

        response = requests.post(
            BASE_URL + "/add_user",
            json=user
        )

        self.assertEqual(response.status_code, 409)
        self.assertEqual(
            response.json(),
            {"error": "Username already exists"}
        )


if __name__ == "__main__":
    unittest.main()
