import unittest
from unittest import TestCase

from api.app import create_app

from flask_sqlalchemy import SQLAlchemy


class UserTestCase(TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = SQLAlchemy(self.app)
        self.db.create_all()
        self.client = self.app.test_client(use_cookies=True)
    
    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()
    
    def test_root_response(self):
        response = self.client.get("/", headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)
