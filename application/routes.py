from application import app, db
from flask import render_template, request, redirect, url_for, Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length
from application.models import Customer, Order, Order_detail, Product
from datetime import datetime

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/product2')
def product2():
    return render_template('prodcut2.html')


@app.route("/categories")
def categories():
    return render_template('category.html')



@app.route('/cart')
def cart():
    all_product = Product.query.all()
    all_orders = Order_detail.query.all()
    total_amount = sum([order.quantity * order.price for order in all_orders])
    return render_template('prodcut2.html', all_orders=all_orders, total_amount=total_amount, all_product=all_product)

 

@app.route('/update_quantity/<int:order_detail_id>', methods=['POST'])
def update_quantity(order_detail_id):
    new_quantity = request.form.get('new_quantity')
    order_detail = Order_detail.query.get(order_detail_id)
    if order_detail:
        order_detail.quantity = int(new_quantity)
        db.session.commit()
    return redirect(url_for('cart'))

 

@app.route('/delete_item/<int:order_detail_id>', methods=['POST'])
def delete_item(order_detail_id):
    order_detail = Order_detail.query.get(order_detail_id)
    if order_detail:
        db.session.delete(order_detail)
        db.session.commit()
    return redirect(url_for('cart'))  # Removed the form object from the redirect


class PayForm(FlaskForm):
    card_num = StringField('Enter 16 digit Card Number', validators=[
        DataRequired(),
        Length(min=16, max=16)])
    cvc_num = StringField('Enter 3 digit CVC Number', validators=[
        DataRequired(),
        Length(min=3, max=3)])    
    submit = SubmitField('Pay Now')

 

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    message = ""
    form = PayForm()
    if request.method == 'POST':
            message = f'Thank you, Payment has been Accepted'
    return render_template('payment.html', form=form, message=message)
 
class ShipForm(FlaskForm):
    first_name = StringField('First Name', validators=[
        DataRequired(),
        Length(min=4, max=30)])
    last_name = StringField('Last Name', validators=[
        DataRequired(),
        Length(min=2, max=30)])
   
    email = StringField('Email', validators=[
        DataRequired(),
        Length(min=2, max=60)])
   
    phone_num = StringField('Enter your phone number', validators=[
        DataRequired(),
        Length(min=5, max=16)])
   
    address = StringField('post code and door number', validators=[
        DataRequired(),
        Length(min=2, max=15)])
    submit = SubmitField('Click here to save your address')

 

@app.route('/shipping', methods=['GET', 'POST'])
def shipping():
    message = ""
    form = ShipForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            phone = form.phone_num.data
            address = form.address.data
            # Create a new Customer instance
            customer = Customer(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                address=address
            )
            # Add and commit the new customer to the database
            db.session.add(customer)
            db.session.commit()
            message = f'Thank you, {first_name} {last_name}. Address was saved'
    return render_template('shipping.html', form=form, message=message)


@app.route('/products', methods=['GET', 'POST'])
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)



@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    product = Product.query.get(product_id)

 

    # Check if there's an active cart for the current session
    cart_order = Order.query.filter_by(is_cart=True, status=True).first()  # Find active cart
    if not cart_order:
        # If no cart, create one
        cart_order = Order(status=True, is_cart=True, order_date=datetime.now())
        db.session.add(cart_order)
        db.session.commit()

 

    if product:
        # Create a new Order_detail instance
        order_detail = Order_detail(
            order_id=cart_order.order_id,
            product_id=product.product_id,
            quantity=1,  # You can modify this to take quantity as an input
            price=product.price
        )

        # Add and commit the new order_detail to the database
        db.session.add(order_detail)
        db.session.commit()
    return redirect(url_for('products'))



@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about_us.html')

@app.route("/product1")
def product1():
    return render_template('product1.html')