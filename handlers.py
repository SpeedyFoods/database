"""
Has the functions that handle the API endpoints. And all the logic for data insertions and queries
"""
import datetime
from multiprocessing import managers
from db_client import db, cursor
from queries.insert_queries import *
from queries.division_query import view_users_ordered_from_every_restaurant_query
from queries.aggregate import *
from queries.nested_aggregation_with_group_by import *
from queries.update import *
from queries.delete import *
from utils.helper import get_random_speeder_id_from_db, get_restaurant_id_by_name, get_user_id_by_email, split_card_number, value_exist_in_column
from tabulate import tabulate


def insert_row(query_name, insert_query, insert_tuple):
    """
    Inserts the values into the table then returns the id/primary key of the last inserted row
    """
    cursor.execute(insert_query, insert_tuple) # CAN THROW ERROR!
    print(f"{query_name} inserted successfully")
    db.commit()
    return cursor.lastrowid

# ---------------FORM HANDLERS---------------
# All form handlers return human readable messages, which notify of failure or success of form submission,
# and potentially a programmer readable message for debugging.

def register_user(user_detail):
    # we should do data validation. right now im able to insert multiple users with the same info. Myabe change some values to UNIQUE?
    
    out = {'msg': "Registered user successfully", 'error': ""}
    
    # removing whitespace from zip and cardnumber
    user_detail['zip'] = user_detail['zip'].replace(' ', '')
    user_detail['card_number'] = user_detail['card_number'].replace(' ', '')

    # print("VALUEEEE",(user_detail))
    try:
        # INSERT USER
        insert_row("User", insert_user_query, (user_detail['first_name'],
            user_detail['last_name'], user_detail['email'], user_detail['phone'], int(user_detail['type'])))

        user_id = get_user_id_by_email(user_detail['email'])

        city = user_detail['city'].lower()
        if(not value_exist_in_column('City', 'city_name', city)):
            insert_row('City', insert_city_query, (city, user_detail['province'] ))

        if (not value_exist_in_column("Zip", 'zip', user_detail['zip'])):
            insert_row("Zip", insert_zip_query, (user_detail['zip'], user_detail['city']))

        unit_number = user_detail["unit_number"] or None # insert NULL value into DB if unit_number was left blank
        insert_row("Address", insert_user_address_query, (user_id, user_detail['zip'], user_detail['building_number'],
            unit_number, user_detail['street_name']))

        # remember to validate cardnumber has 16 digits
        [card_number_6,card_number_rest] = split_card_number(user_detail['card_number'])

        if (not value_exist_in_column('Card_BIN', 'card_number_6', card_number_6)):
            insert_row("Card_BIN", insert_card_bin_query, (card_number_6,
                user_detail['bank_name'], user_detail['card_type'],
                user_detail['payment_system']))

        insert_row("Card_All", insert_card_all_query, (card_number_6,
            card_number_rest, user_detail['expiration_date'],
            user_detail['zip'], user_id))
    
    except Exception as e:
        print(e)
        out['msg'] = 'Failed to register user'
        out['error'] = e
    
    return out

def register_restaurant(restaurant_detail):
    out = {'msg': "Regiestered restaurant successfully", 'error': ""}
    try:
        # discuss: can one manger have multiple 
        manager_id = get_user_id_by_email(restaurant_detail['restaurant_manager_email'])
        # manager_id = randint(100,999)

        if (manager_id == None):
            # manager_id = randint(100,500)
            out['msg'] = f"User with email {restaurant_detail['restaurant_manager_email']} does not Exist"
            return out
        
        if (value_exist_in_column('Restaurant', 'restaurant_id', manager_id)):
            out['msg'] = f"This user is already managing a restaurant"
            return out
        
        if (not value_exist_in_column('RestaurantParent', 'restaurant_name', restaurant_detail['restaurant_name'])):
            insert_row("Restaurant Parent", insert_restaurant_parent_query,
                    (restaurant_detail['restaurant_name'], restaurant_detail['cuisine']))

        insert_row("Restaurant", insert_restaurant_query, (manager_id, restaurant_detail['restaurant_name']))

    except Exception as e:
        print(e)
        out['msg'] = "Failed to register restaurant"
        out['error'] = e
    
    return out

def insert_restaurant_item(register_item_detail):
    out = {'msg': "Inserted restaurant item successfully", 'error': ""}

    try:
        restaurant_id = get_restaurant_id_by_name(register_item_detail['restaurant_name'])
        insert_row("Item", insert_item_query, (register_item_detail['item_name'], restaurant_id, register_item_detail['price']))
    except Exception as e:
        out['msg'] = "Failed to insert restaurant item"
        out['error'] = e
        print(e)
    
    return out


def place_order(order_detail):
    out = {'msg': "Placed order successfully", 'error': ""}
    try:
        consumer_id = get_user_id_by_email(order_detail['consumer_email'])
        restaurant_id = get_restaurant_id_by_name(order_detail['restaurant_name'])
        print(consumer_id, restaurant_id)

        order_id = insert_row("_Order", insert_order_query,
                (order_detail['tip'],0 , datetime.datetime.now(), order_detail['special_instructions'], consumer_id, restaurant_id, get_random_speeder_id_from_db()))

        insert_row("Order to Item", insert_order_to_item_query,
                    (order_id, restaurant_id, order_detail['item_name']))
    except Exception as e:
        out['msg'] = "Failed to place order"
        out['error'] = e
        print(e)
    
    return out

def rate_restaurant(user_detail):

    # insert_user_to_user_reviews_query = """
    # INSERT INTO UserToUser_Reviews (
    # user_id_ratable, 
    # user_id_consumer, 
    # rating_time,
    # value,
    # review
    # )
    # VALUES (%s, %s, %s, %s, %s)
    # """
    # remember to implement try catch
    # find the user id ratable by doing a select search statemet
    user_id_ratable = user_detail['restaurant']
    consumer_id1 = get_user_id_by_email(user_detail['cons_email1'])
    # find the user_id_consumer ratable by doing a select search statemet

    insert_row("user to user reviews", insert_user_to_user_reviews_query, (user_id_ratable,
                consumer_id1, user_detail['value'], user_detail['review']))

# --------------------------------------------------
# Select queries here?

def table_from_cursor(cursor):
    """
    returns html table as a string
    """
    myresult = cursor.fetchall()
    field_names = [i[0] for i in cursor.description]
    html = tabulate(myresult, tablefmt='html', headers=field_names)
    return html

def view_users():
    """
    goal is to return a list of user detail
    """
    cursor.execute("select * from User;")
    return table_from_cursor(cursor)


def view_restaurants():
    cursor.execute("select * from Restaurant;")
    return table_from_cursor(cursor)

def view_restaurant_items(restaurant_name):
    # check if restaurant exists, if not, return "Restaurant not in database"
    # cursor.execute(f"select * from Restaurant where restaurant_name = '{restaurant_name}';")
    cursor.execute(f"select item_name, price from Restaurant, Item where restaurant_name = '{restaurant_name}' and Restaurant.restaurant_id = Item.restaurant_id;")
    return table_from_cursor(cursor)

    # else, return html
    # return "items table"

def view_orders():
    # select all orders and return it
    cursor.execute("select * from _Order;")
    return table_from_cursor(cursor)
    # return "orders"

def view_users_ordered_from_every_restaurant():
    cursor.execute(view_users_ordered_from_every_restaurant_query)
    return table_from_cursor(cursor)

def aggregate_query():
    cursor.execute(select_average_price_of_all_items)
    return table_from_cursor(cursor)

def cheapest_item_every_query():
    cursor.execute(cheapest_item_every)
    return table_from_cursor(cursor)
    
def update_user_email(data):
    print(data)
    cursor.execute(update_user_email_query % (data['user_email'], int(data['user_id'])))
    db.commit()
    return True


def delete_user_by_id(data):
    print(data)
    cursor.execute(delete_user_by_id_query % data['user_id'])
    db.commit()
    return True

if __name__ == "__main__":
    # view_restaurants()
    pass