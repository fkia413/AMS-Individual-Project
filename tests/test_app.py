import pytest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from flask_bcrypt import generate_password_hash,check_password_hash
from application.models import Customer, Order, Product, Order_detail

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///testdata.db',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app
    
def setUp(self):
     db.drop_all()
     db.create_all()
