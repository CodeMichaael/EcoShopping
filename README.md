# EcoShopping
An example framework for a shopping API or system.

# Examples
```py
from flask import Flask, request, jsonify
from typing import List
from shop import ShopManager
from listings import ListingManager

app = Flask(__name__)

# Initialize the managers
shop_manager = ShopManager(admin=True)
listing_manager = ListingManager(admin_mode=True)

# Shop API

@app.route('/add_item/<store_id>', methods=['POST'])
def add_item(store_id):
    try:
        data = request.get_json()
        items = data['items']  # List of items to add
        shop_manager.add_items(items, store_id)
        return jsonify(message="Items added successfully"), 201
    except ValueError as e:
        return jsonify(error=str(e)), 400

@app.route('/get_items/<store_id>', methods=['GET'])
def get_items(store_id):
    try:
        items = shop_manager.get_items(store_id)
        return jsonify(items=items)
    except ValueError as e:
        return jsonify(error=str(e)), 404

# Listing API

@app.route('/new_listing/<listing_name>', methods=['POST'])
def new_listing(listing_name):
    try:
        data = request.get_json()
        items = data['items']  # List of items for the new listing
        listing_manager.get_new_listing(listing_name, items)
        return jsonify(message="New listing created successfully"), 201
    except ValueError as e:
        return jsonify(error=str(e)), 400

@app.route('/search_listing/<listing_name>', methods=['GET'])
def search_listing(listing_name):
    result = listing_manager.search_listing(listing_name)
    if result:
        return jsonify(items=result)
    else:
        return jsonify(message="Listing not found"), 404

if __name__ == '__main__':
    app.run(debug=True)
```
