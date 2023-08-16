from flask import url_for
from flask_testing import TestCase
from flask_bcrypt import generate_password_hash,check_password_hash
from application import app, db 
from application.models import Order, Order_Product, Product,Customer

class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.drop_all()
        db.create_all()
        # Create test registree
        poker_table_red = Product(name='Poker Table (Red)',category='Tables',price=49.99,stock=10,desc='This is an 9 player poker table with black leather rim and red felt.',image='2.png')
        poker_table_green = Product(name='Poker Table (Green)',category='Tables',price=39.99,stock=10,desc='This is a 6 person poker table with Blacker leather rim and green felt.',image='1.png')
        playing_card_red = Product(name='Playing Cards (Red)',category='Cards',price=6.99,stock=5,desc='This is a red pack of plastic Bicycle playing cards.',image='3.png')
        playing_card_blue = Product(name='Playing Cards (Blue)',category='Cards',price=6.99,stock=0,desc='This is a blue pack of plastic Bicycle playing cards.',image='4.png')

        new_cust = Customer()
        new_order = Order(customerbr = new_cust)
        # save users to database
        db.session.add(poker_table_green)
        db.session.add(poker_table_red)
        db.session.add(playing_card_blue)
        db.session.add(playing_card_red)
        db.session.add(new_cust)
        db.session.add(new_order)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    
    def test_product_listing_get(self):
        response = self.client.get(url_for('product_listing'))
        self.assertEqual(response.status_code, 200)

    def test_categories_get(self):
        response = self.client.get(url_for('categories'))
        self.assertEqual(response.status_code, 200)

    def test_cart_get(self):
        response = self.client.get(url_for('cart'))
        self.assertEqual(response.status_code, 200)
    
    def test_checkout_get(self):
        response = self.client.get(url_for('checkout'))
        self.assertEqual(response.status_code, 200)

    def test_payment_get(self):
        response = self.client.get(url_for('payment'))
        self.assertEqual(response.status_code, 200)
    
    def test_contact_get(self):
        response = self.client.get(url_for('contacts'))
        self.assertEqual(response.status_code, 200)

    def test_about_us_get(self):
        response = self.client.get(url_for('about_us'))
        self.assertEqual(response.status_code, 200)
    
    def test_pay_success_get(self):
        response = self.client.get(url_for('pay_success'))
        self.assertEqual(response.status_code, 200)

    def test_single_prod_get(self):
        for i in Product.query.all():
            response = self.client.get(url_for('single_product', id=i.id))
            self.assertEqual(response.status_code, 200)


class TestCrud(TestBase):

    def test_categories_post(self):
        response = self.client.post(url_for('categories'), data = dict(category='Cards'))

        test_objs = Product.query.filter_by(category='Cards').all()
        for test_obj in test_objs:
            self.assertEqual(test_obj.category,'Cards')

    def test_cart_post(self):
        pass

    def test_checkout_post(self):
        response = self.client.post(url_for('checkout'), data = dict(line1='line1',line2='line2',line3='line3',city='city',pc='postcode'))

        test_obj = Customer.query.filter_by(add_line1='line1',add_line2='line2',add_line3='line3',city='city',postcode='postcode').first()
        
        self.assertEqual(test_obj.add_line1,'line1')
        self.assertEqual(test_obj.add_line2,'line2')
        self.assertEqual(test_obj.add_line3,'line3')
        self.assertEqual(test_obj.city,'city')
        self.assertEqual(test_obj.postcode,'postcode')

    def test_payments_post(self):
        response = self.client.post(url_for('payment'), data = dict(card_name='card_name',card_no='1234567890123456',exp1='01',exp2='29',cvv='123'))

        test_obj = Customer.query.filter_by(card_name='card_name').first()
        
        self.assertEqual(test_obj.card_name,'card_name')
        self.assertEqual(check_password_hash(test_obj.card_no, '1234567890123456'),True)
        self.assertEqual(test_obj.card_exp,'01/29')
        self.assertEqual(check_password_hash(test_obj.cvv,'123'),True)

    def test_single_product_post(self):
        for i in Product.query.all():
            response = self.client.post(url_for('single_product', id=i.id), data = dict(amount = '1'))

            basket = Order.query.filter_by(is_complete=False).first()
            test_obj = Order_Product.query.filter_by(amount = '1', prod_id = i.id, order_id=basket.id).first()
            
            self.assertEqual(test_obj.amount,1)



    