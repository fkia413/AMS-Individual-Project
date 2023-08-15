from application import db
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(30), nullable =False)
    orders = db.relationship('Basket', backref='customer')

class Basket(db.Model):
    basket_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    order_date = db.Column(db.DateTime)
    order_status = db.Column(db.Boolean)
    basket_details = db.relationship('Basket_details', backref='basket') 

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float)
    stock_quantity = db.Column(db.Integer)
    basket_details = db.relationship('Basket_details', backref='product')

class Basket_details(db.Model):
    basket_details_id = db.Column(db.Integer, primary_key=True)
    backet_id = db.Column(db.Integer, db.ForeignKey('basket.basket_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable = False)
    price = db.Column(db.Float, nullable=False)
