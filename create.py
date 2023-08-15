from application import db, app
from application.models import Customer, Order, Product, Order_detail
from application import routes


with app.app_context():
    db.drop_all()
    db.create_all()

    banana = Product(name="banana", description="its a nice bananana", price=10, stock_quantity=7)
    db.session.add(banana)
    db.session.commit()

    apple = Product(name="apple", description="its a nice apple", price=30, stock_quantity=100)
    db.session.add(apple)
    db.session.commit()

    pear = Product(name="pear", description="its a nice pear", price=50, stock_quantity=100)
    db.session.add(pear)
    db.session.commit()

    testuser = Order_detail(order_id=1, product=banana, quantity=10)
    testuser.price = banana.price 
    db.session.add(testuser)
    db.session.commit()

    testapple = Order_detail(order_id=2, product=apple, quantity=5)
    testapple.price = apple.price 
    db.session.add(testapple)
    db.session.commit()

    testuser = Order_detail(order_id=3, product=pear, quantity=6)
    testuser.price = pear.price
    db.session.add(testuser)
    db.session.commit()