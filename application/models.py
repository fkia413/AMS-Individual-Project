class Customer(db.Model):

    customer_id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(30), nullable=False)

    last_name = db.Column(db.String(30), nullable=False)

    email = db.Column(db.String(30), nullable=False)

    phone = db.Column(db.Integer, nullable=False)

    address = db.Column(db.String(30), nullable =False)

    orders = db.relationship('Order', backref='customer')

 

class Order(db.Model):

    order_id = db.Column(db.Integer, primary_key=True)

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)

    order_date = db.Column(db.DateTime)

    status = db.Column(db.Boolean) ### db.Column(db.String(30), nullable=False)

 

 

class Product(db.Model):

    product_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(30), nullable=False)

    description = db.Column(db.String(30), nullable=False)

    price = db.Column(db.Float)

    stock_level = db.Column(db.Integer)

 

class Order_detail(db.Model):

    order_detail = db.Column(db.Integer, primary_key=True)

    order_fid = db.Column(db.Integer, db.ForigenKey('order'))

    product_fid = db.Column(db.Integer, db.ForigenKey('product'))

    quantity = db.Column(db.Integer)

    price = db.Column(db.Float)