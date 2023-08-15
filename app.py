from application import app
from flask import Flask, jsonify

app = Flask(__name__)

# Assuming you have an SQLite database connection established

@app.route('/api/cart')
def get_cart_items():
    # Fetch cart items from the database
    # Replace this with your actual database query
    cart_items = [
        { "id": 1, "name": "Product A", "price": 20, "quantity": 2 },
        { "id": 2, "name": "Product B", "price": 15, "quantity": 1 },
        # Add more items as needed
    ]
    return jsonify(cart_items)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')