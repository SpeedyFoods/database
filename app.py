"""
application to run the python flask server
"""

from flask import Flask, render_template
from flask import request
from flask_expects_json import expects_json
from utils.create_tables import create_tables

from handlers import insert_restaurant_item, register_user, register_restaurant, place_order, rate_restaurant
from utils.insert_single_rows import insert_sample_rows

app = Flask(__name__)

from db_client import db, cursor

@app.route('/')
def hello_world():
    return render_template(
            'home.html',
            title="Home",
            description="Order Now!"
        )

Register_User_Schema = {
  "type": "object",
  "properties": {
    # user details
    "first_name": { "type": "string" },
    "last_name": { "type": "string" },
    "email": { "type": "string" },
    "phone": { "type": "number" },
    "type": { "type": "number" },
    # address info
    "zip": { "type": "string" },
    "city": { "type": "string" },
    "province": { "type": "string" },
    "building_number": { "type": "number" },
    "unit_number": { "type": "number" },
    "street_name": { "type": "string" },
    # card number info
    "card_number": { "type": "string" },
    "expiration_date": { "type": "number" }, 
  },
  "required": [
    "first_name",
    "last_name",
    "email",
    "phone",
    "type",
    "zip",
    "building_number",
    "unit_number",
    "street_name",
    "card_number",
    "expiration_date",
  ]
}
@app.route('/user_sign_up', methods=['POST'])
@expects_json(Register_User_Schema)
def route_register_user():
    user_details = request.get_json(force=True)
    try:
      result = register_user(user_details)
      return result
    except Exception as e:
      print(e)

Register_Restaurant_Schema = {
  "type": "object",
  "properties": {
    "restaurant_manager_email": { "type": "string" },
    "restaurant_name": { "type": "string" },
    "cuisine": { "type": "string" },
  },
}
@app.route('/register_restaurant', methods=['POST'])
@expects_json(Register_Restaurant_Schema)
def route_register_restaurant():
    restaurant_details = request.get_json(force=True)
    register_restaurant(restaurant_details)
    return restaurant_details


Restaurant_Item_Schema = {
  "type": "object",
  "properties": {
    "item_name": { "type": "string" },
    "restaurant_name": { "type": "string" },
    "price": { "type": "number" },
    "user_email": { "type": "string" },
  },
}
@app.route('/insert_restaurant_item', methods=['POST'])
@expects_json(Restaurant_Item_Schema)
def route_restaurant_item():
    restaurant_item = request.get_json(force=True)
    insert_restaurant_item(restaurant_item)
    return restaurant_item

# Place an order
# discuss: we have to think how we want our data
Place_Order_Schema = {
  "type": "object",
  "properties": {
    "tip": { "type": "string" },
    "status": { "type": "string" },
    "special_instructions": { "type": "string" },
    "consumer_email": { "type": "string" },
    "restaurant_name": { "type": "string" },
    "item_name": { "type": "string" },
  },
}
@app.route('/place_order', methods=['POST'])
@expects_json()
def route_place_order():
    order_details = request.get_json(force=True)
    place_order(order_details)
    return order_details


# Place an order
Rate_Restaurant_Schema = {
  "type": "object",
  "properties": {
    "tip": { "type": "string" },
    "restaurant": { "type": "string" },
    "user_email": { "type": "string" },
    "rating_time": { "type": "string" },
    "value": { "type": "string" },
    "review": { "type": "string" },
  },
}
@app.route('/rate_restaurant', methods=['POST'])
@expects_json()
def route_rate_restaurant():
    rating_details = request.get_json(force=True)
    rate_restaurant(rating_details)
    return rating_details


# discussion
@app.route('/reset_database', methods=['GET'])
def reset_database():
    create_tables()
    return "database reset"