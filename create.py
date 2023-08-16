from application import db, app
from application.models import Customer, Order, Product, Order_detail
from application import routes


with app.app_context():
    db.drop_all()
    db.create_all()

    hoodie = Product(name="One Piece Puffy Pink Hoodie", description="The comfiest hoodie you will ever wear! Make your uncle jealous.", price=150, stock_quantity=7)
    db.session.add(hoodie)
    db.session.commit()

    mug = Product(name="One Piece Mega Massive Mug", description="This mug makes water taste like coca cola. Try it now! [CAUTION: MAY BE POISONOUS]", price=3, stock_quantity=100)
    db.session.add(mug)
    db.session.commit()

    shoes = Product(name="One Piece 'Wings of Freedom' Trainers", description="These shoes will let you fly! [DO NOT TRY THIS]", price=50, stock_quantity=100)
    db.session.add(shoes)
    db.session.commit()

    mascot = Product(name="One Piece Rudolph the Reindeer Mascot", description="The cutest mascot you will ever own. [DO NOT PLACE IN WATER OR IT WILL MULTIPLY]", price=20, stock_quantity=100)
    db.session.add(mascot)
    db.session.commit()

    testuser = Order_detail(order_id=1, product=hoodie, quantity=10)
    testuser.price = hoodie.price 
    db.session.add(testuser)
    db.session.commit()

    testapple = Order_detail(order_id=2, product=mug, quantity=5)
    testapple.price = mug.price 
    db.session.add(testapple)
    db.session.commit()

    testuser = Order_detail(order_id=3, product=shoes, quantity=6)
    testuser.price = shoes.price
    db.session.add(testuser)
    db.session.commit()

    testuser = Order_detail(order_id=3, product=mascot, quantity=6)
    testuser.price = mascot.price
    db.session.add(testuser)
    db.session.commit()