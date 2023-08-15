from application import app, db, __init__
from flask import render_template, request, redirect, url_for, Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length
from application.models import Customer, Basket, Basket_details, Product


@app.route('/')
def home():
    return render_template ('index.html')


@app.route("/products")
def prodcuts():
    return render_template('products.html')

@app.route("/categories")
def categories():
    return render_template('categories.html')

@app.route("/checkout")
def shipping():
    return render_template('checkout.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about_us.html')

@app.route('/cart')
def cart():
    all_product = Product.query.all()
    all_orders = Basket_details.query.all()
    total_amount = sum([order.quantity * order.price for order in all_orders])
    return render_template('cart.html', all_orders=all_orders, total_amount=total_amount, all_product=all_product)

 

@app.route('/update_quantity/<int:basket_details_id>', methods=['POST'])
def update_quantity(basket_detailsid):
    new_quantity = request.form.get('new_quantity')
    basket_details = Basket_details.query.get(basket_details.id)
    if basket_details:
        basket_details.quantity = int(new_quantity)
        db.session.commit()
    return redirect(url_for('cart'))

 

@app.route('/delete_item/<int:basket_details_id>', methods=['POST'])
def delete_item(basket_details_id):
    basket_details = Basket_details.query.get(basket_details_id)
    if basket_details:
        db.session.delete(basket_details)
        db.session.commit()
    return redirect(url_for('cart'))  # Removed the form object from the redirect


class PayForm(FlaskForm):
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

 

            message = f'Thank you, {first_name} {last_name}. Payment Accepted' 
    return render_template('payment.html', form=form, message=message)
