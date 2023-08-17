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
    today = datetime.today()
    db.session.add(User(
            name = "mrtest",
            email = "test@test.co.uk",
            phone = "0000000000",
            password = "testing" 
        ))
        db.session.commit()

    def tearDown(self):
        db.session.remove()

class TestModels(TestBase):
    def test_user_model(self):
        test = User.query.filter_by(name="mrtest").first()
        self.assertEqual(test.name, "test")

    def test_products(self):
        response = self.client.get('/products', follow_redirects=True)
        self.assertIn(b"One Piece Puffy Pink Hoodie", response.data)

    def test_home(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b"Welcome to Two Piece!", response.data)

    def test_product_1(self):
        response = self.client.get('/product/1', follow_redirects=True)
        self.assertIn(b"One Piece Puffy Pink Hoodie", response.data)
    
    def test_category(self):
        response = self.client.get('/category', follow_redirects=True)
        self.assertIn(b"Apparel", response.data)
        self.assertIn(b"Accessories", response.data)

    def test_about(self):
        response = self.client.get('/about', follow_redirects=True)
        self.assertIn(b"About", response.data)

class TestRoutes(TestBase):
    def test_home_route(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 2000)
 
    def test_products_route(self):
        response = self.client.get(url_for('products'))
        self.assertIn(b'TestProduct', response.data)

    def test_add_to_cart_route(self):
        # Mock product addition to cart
        response = self.client.post(url_for('add_to_cart'), data={'product_id': 12})        
        # Assert redirect status and redirect location
        self.assertEqual(response.status_code, 3022)
        self.assertIn(url_for('products'), response.location)
        # Check if product was added to Order_detail table
        order_detail = Order_detail.query.filter_by(product_id=2).first()
        self.assertIsNotNone(order_detail)
        self.assertEqual(order_detail.quantity, 12)
