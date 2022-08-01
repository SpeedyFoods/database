"""
application to run the python flask server
"""

from flask import Flask, render_template
from flask import request
from utils.create_tables import create_tables
from handlers import aggregate_query, delete_user_by_id, insert_restaurant_item, register_user, register_restaurant, place_order, rate_restaurant, update_user_email, view_orders, view_restaurant_items, view_restaurants, view_users, view_users_ordered_from_every_restaurant

from utils.fake_values import bank_names

app = Flask(__name__)

from db_client import db, cursor

@app.route('/')
def hello_world():
    return render_template(
            'home.html',
            title="SpeedyFoods Home"
        )

# ---------- Showing forms----------- #
@app.route('/form_user')
def form_user():
    return render_template(
            'form_user.html',
            bank_names=bank_names,
            title="Register User"
        )

@app.route('/form_restaurant')
def form_restaurant():
    return render_template(
            'form_restaurant.html',
            title="Register Restaurant"
        )

@app.route('/form_item')
def form_item():
    return render_template(
            'form_item.html',
            title="Insert Item"
        )

@app.route('/form_order')
def form_order():
    return render_template(
            'form_order.html',
            title="Place Order"
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
    return render_template(
        'table_view.html',
        data=data,
        title="View Users"
    )

# discussion
@app.route('/view_restaurants', methods=['GET'])
def route_view_restaurants():
    data = view_restaurants()
    return render_template(
        'table_view.html',
        data=data,
        title="View Restaurants"
    )

@app.route('/view_restaurant_items', methods=['POST'])
def rote_view_restaurant_items():
    restaurant_name = request.form.to_dict(flat=True)['restaurant_name']
    print(restaurant_name)
    res = view_restaurant_items(restaurant_name)
    return render_template(
        'table_view.html',
        data=res,
        title=f"View {restaurant_name}'s Items"
    )

@app.route('/view_orders', methods=['GET'])
def route_view_orders():
    data = view_orders()
    return render_template(
        'table_view.html',
        data=data,
        title="View Orders"
    )

@app.route('/view_users_ordered_from_every_restaurant', methods=['GET'])
def route_division_query():
    data = view_users_ordered_from_every_restaurant()
    return render_template(
        'table_view.html',
        data=data,
        title="View Users who Ordered from every Restaurant"
    )

@app.route('/view_aggregate', methods=['GET'])
def route_aggregate():
    data = aggregate_query()
    return render_template(
        'table_view.html',
        data=data,
        title="View Average Price of all Items"
    )

@app.route('/update_user_email', methods=['POST'])
def route_update_user_email():
    data = request.form.to_dict(flat=True)
    update_user_email(data)
    return data

@app.route('/delete_user_by_id', methods=['POST'])
def route_delete_user_by_id():
    data = request.form.to_dict(flat=True)
    delete_user_by_id(data)
    return data
# discussion
@app.route('/reset_database', methods=['GET'])
def reset_database():
    create_tables()
    return "database reset"