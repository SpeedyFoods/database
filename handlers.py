"""
Has the functions that handle the API endpoints
"""
import datetime
from multiprocessing import managers
from random import randint
from db_client import db, cursor
from queries.insert_queries import *
from utils.helper import get_random_speeder_id_from_db, get_restaurant_id_by_name, get_user_id_by_email, split_card_number, value_exist_in_column
from tabulate import tabulate


def insert_row(query_name, insert_query, insert_tuple):
    """
    Inserts the values into the table then returns the id/primary key of the last inserted row
    """
    try:
        cursor.execute(insert_query, insert_tuple)
        print(f"{query_name} inserted successfully")
        db.commit()
        return cursor.lastrowid
    except Exception as e:
        print(e)
        print(f"failed to insert to table {query_name}")

def register_user(user_detail):
    # we should do data validation. right now im able to insert multiple users with the same info. Myabe change some values to UNIQUE?
    res = {}
    res['success'] = False
    res['error'] = "no errors"

    try:
        # INSERT USER
        insert_row("User", insert_user_query, (user_detail['first_name'],
            user_detail['last_name'], user_detail['email'], user_detail['phone'], user_detail['type']))

        user_id = get_user_id_by_email(user_detail['email'])

        city = user_detail['city'].lower()
        if(not value_exist_in_column('City', 'city_name', city)):
            insert_row('City', insert_city_query, (city, user_detail['province'] ))

        if (not value_exist_in_column("Zip", 'zip', user_detail['zip'])):
            insert_row("Zip", insert_zip_query, (user_detail['zip'], user_detail['city']))

        insert_row("Address", insert_user_address_query, (user_id, user_detail['zip'], user_detail['building_number'],
            user_detail['unit_number'], user_detail['street_name']))

        # remember to validate cardnumber has 16 digits
        [card_number_6,card_number_rest] = split_card_number(user_detail['card_number'])

        if (not value_exist_in_column('Card_BIN', 'card_number_6', card_number_6)):
            insert_row("Card_BIN", insert_card_bin_query, (card_number_6,
                user_detail['bank_name'], user_detail['card_type'],
                user_detail['payment_system']))

        insert_row("Card_All", insert_card_all_query, (card_number_6,
            card_number_rest, user_detail['expiration_date'],
            user_detail['zip'], user_id))

        res['success'] = True
        return res

    # i think there is a better way to catch error messages
    except Exception as e:
        res['error'] = "Failed to insert user data" + str(e)
        print("Failed to insert user data")
        print(e)
        return res

def register_restaurant(restaurant_detail):
    res = {}
    res['success'] = False
    res['error'] = "no errors"
    try:
        # discuss: can one manger have multiple 
        manager_id = get_user_id_by_email(restaurant_detail['restaurant_manager_email'])
        # manager_id = randint(100,999)

        if (manager_id == None):
            # manager_id = randint(100,500)
            res['error'] = f"User with email {restaurant_detail['restaurant_manager_email']} does not Exist"
            res['success'] = False
            print( f"User with email {restaurant_detail['restaurant_manager_email']} does not Exist")
            return res
        if (value_exist_in_column('Restaurant', 'restaurant_id', manager_id)):
            res['error'] = f"This user is already managing a restaurant"
            res['success'] = False
            return res

        if (not value_exist_in_column('RestaurantParent', 'restaurant_name', restaurant_detail['restaurant_name'])):
            insert_row("Restaurant Parent", insert_restaurant_parent_query,
                    (restaurant_detail['restaurant_name'], restaurant_detail['cuisine']))

        insert_row("Restaurant", insert_restaurant_query, (manager_id, restaurant_detail['restaurant_name']))
        return res

    except Exception as e:
        res['error'] = "Failed to insert user data" + str(e)
        print("Failed to register user")
        print(e)
        return res


def insert_restaurant_item(register_item_detail):
    res = {}
    res['success'] = False
    res['error'] = "no errors"
    try:
        restaurant_id = get_restaurant_id_by_name(register_item_detail['restaurant_name'])
        insert_row("Item", insert_item_query, (register_item_detail['item_name'], restaurant_id, register_item_detail['item_name']))
    except Exception as e:
        res['error'] = "Failed to insert user data" + str(e)
        print("Failed to insert restaurant item")
        print(e)
        return res
    return res


# def get_order_id_
def place_order(order_detail):
    res = {}
    res['success'] = False
    res['error'] = "no errors"
    try:
        consumer_id = get_user_id_by_email(order_detail['consumer_email'])
        restaurant_id = get_restaurant_id_by_name(order_detail['restaurant_name'])

        order_id = insert_row("_Order", insert_order_query,
                (order_detail['tip'],0 , datetime.datetime.now(), order_detail['special_instructions'], consumer_id, restaurant_id, get_random_speeder_id_from_db()))

        insert_row("Order to Item", insert_order_to_item_query,
                    (order_id, restaurant_id, order_detail['item_name']))
    except Exception as e:
        res['error'] = "Failed to insert user data" + str(e)
        print("Failed to place order" + str(e))
        print(e)
        return res

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
                consumer_id1, user_detail['rating_time'], user_detail['value'], user_detail['review']))

# --------------------------------------------------
# Select queries here?

def view_users():
    """
    goal is to return a list of user detail
    """
    cursor.execute("select * from User;")
    myresult = cursor.fetchall()
    html = tabulate(myresult, tablefmt='html')
    print(html)
    return html


def view_restaurants():
    cursor.execute("select * from Restaurant;")
    myresult = cursor.fetchall()
    html = tabulate(myresult, tablefmt='html')
    return html

def view_restaurant_items(restaurant_name):
    # check if restaurant exists, if not, return "Restaurant not in database"
    # cursor.execute(f"select * from Restaurant where restaurant_name = '{restaurant_name}';")
    cursor.execute(f"select * from Restaurant, Item where restaurant_name = '{restaurant_name}' and Restaurant.restaurant_id = Item.restaurant_id;")
    myresult = cursor.fetchall()
    html = tabulate(myresult, tablefmt='html')
    return html

    # else, return html
    # return "items table"

def view_orders():
    # select all orders and return it
    cursor.execute("select * from _Order;")
    myresult = cursor.fetchall()
    html = tabulate(myresult, tablefmt='html')
    return html
    # return "orders"

if __name__ == "__main__":
    view_restaurants()