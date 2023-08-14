from application import app, db
from application.models import Customer,Order,Product,Order_detail
from flask import render_template, request

@app.route('/')
def home():
    return render_template ('index.html')


@app.route("/products")
def prodcuts():
    return render_template('products.html')

@app.route("/categories")
def categories():
    return render_template('category.html')

@app.route('/cart')
def cart():
    all_orders = Order_detail.query.all()
    total_amount = 0
    for order in all_orders:
        total_amount += order.quantity * order.price
    return render_template('prodcut2.html', all_orders=all_orders, total_amount=total_amount)

@app.route("/shipping")
def shipping():
    return render_template('shipping.html')

@app.route("/payment")
def payment():
    return render_template('payment.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about_us.html')