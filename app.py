"""
application to run the python flask server
"""

from flask import Flask, render_template
from flask import request
from flask_expects_json import expects_json
from utils.create_tables import create_tables

from handlers import insert_restaurant_item, register_user, register_restaurant, place_order, rate_restaurant, view_orders, view_restaurant_items, view_restaurants, view_users
from utils.insert_single_rows import insert_sample_rows

from utils.fake_values import bank_names

app = Flask(__name__)

from db_client import db, cursor

@app.route('/')
def hello_world():
    return render_template(
            'home.html'
        )

# ---------- Showing forms----------- #
@app.route('/form_user')
def form_user():
    return render_template(
            'form_user.html',
            bank_names=bank_names
        )

@app.route('/form_restaurant')
def form_restaurant():
    return render_template(
            'form_restaurant.html',
        )

@app.route('/form_item')
def form_item():
    return render_template(
            'form_item.html',
        )

@app.route('/form_order')
def form_order():
    return render_template(
            'form_order.html',
        )
# ------------------------------------ #
 
# EXPECTED VALUES FROM THE FORM
  # "properties": {
  #   # user details
  #   "first_name": { "type": "string" },
  #   "last_name": { "type": "string" },
  #   "email": { "type": "string" },
  #   "phone": { "type": "number" },
  #   "type": { "type": "number" },
  #   # address info
  #   "zip": { "type": "string" },
  #   "city": { "type": "string" },
  #   "province": { "type": "string" },
  #   "building_number": { "type": "number" },
  #   "unit_number": { "type": "number" },
  #   "street_name": { "type": "string" },
  #   # card number info
  #   "card_number": { "type": "string" },
  #   "expiration_date": { "type": "number" }, 
  # },
@app.route('/user_sign_up', methods=['GET','POST'])
def route_register_user():
    data =request.form.to_dict(flat=True)
    try:
      result = register_user(data)
      return result
    except Exception as e:
      print(e)

# EXPECTED VALUES FROM THE FORM
# "restaurant_manager_email": { "type": "string" },
# "restaurant_name": { "type": "string" },
# "cuisine": { "type": "string" },
@app.route('/register_restaurant', methods=['GET','POST'])
def route_register_restaurant():
    data =request.form.to_dict(flat=True)
    print(data)
    res = register_restaurant(data)
    if not res['success']:
      return res['error']
    return 'success'
  

# EXPECTED VALUES FROM THE FORM
# "item_name": { "type": "string" },
# "restaurant_name": { "type": "string" },
# "price": { "type": "number" },
@app.route('/insert_restaurant_item', methods=['POST'])
def route_restaurant_item():
    data =request.form.to_dict(flat=True)
    insert_restaurant_item(data)
    return "Success"

# EXPECTED VALUES FROM THE FORM
# "tip": { "type": "string" },
# "status": { "type": "string" },
# "special_instructions": { "type": "string" },
# "consumer_email": { "type": "string" },
# "restaurant_name": { "type": "string" },
# "item_name": { "type": "string" },
@app.route('/place_order', methods=['POST'])
def route_place_order():
    data =request.form.to_dict(flat=True)
    place_order(data)
    return data


# EXPECTED VALUES FROM THE FORM
@app.route('/rate_restaurant', methods=['POST'])
def route_rate_restaurant():
    data = request.form.to_dict(flat=True)
    rate_restaurant(data)
    return data

# discussion
@app.route('/view_users', methods=['GET'])
def route_view_users():
    data = view_users()
    return data

# discussion
@app.route('/view_restaurants', methods=['GET'])
def route_view_restaurants():
    data = view_restaurants()
    return data

@app.route('/view_restaurant_items', methods=['POST'])
def rote_view_restaurant_items():
    restaurant_name = request.form.to_dict(flat=True)['restaurant_name']
    print(restaurant_name)
    res = view_restaurant_items(restaurant_name)
    return res

@app.route('/view_orders', methods=['GET'])
def route_view_orders():
    data = view_orders()
    return data

# discussion
@app.route('/reset_database', methods=['GET'])
def reset_database():
    create_tables()
    return "database reset"