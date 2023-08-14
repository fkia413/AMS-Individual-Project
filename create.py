from application import db, app
from application.models import Customer,Order,Product,Order_detail
with app.app_context():
    db.drop_all()
    db.create_all()

    testuser = Order_detail(order_id=1, product_id=1, quantity=10, price=12.50)
    db.session.add(testuser)
    db.session.commit()