"""
This file is a script that helps us populate all data(rows) to all of our Tables. 
a file that helps us insert bulk data to our database using our main funcitons from handlers.py
"""

from utils.fake_values import list_of_dishes, list_of_cuisine, restaurant_names, fake_names, email_providers, bc_cities, fake_street_names, bank_names, debit_credit, visa_mastercard
from random import randint, choice
from db_client import cursor
from handlers import get_restaurant_id_by_name, insert_restaurant_item, insert_row, place_order, register_restaurant, register_user, rate_restaurant
from utils.helper import generate_fake_zip, get_random_item_from, get_random_item_from_restaurant, get_random_restaurant_from_db, get_random_user_email_from_db
from queries.insert_queries import insert_speeder_query

def populate_register_user():
    """
    insert 10 random user data information to the tables User, Address, Zip, Card_BIN, Card_All
    """
    for _ in range(20):
        [first_name, last_name] = get_random_item_from(fake_names)
        fake_user_details = {
            "first_name": first_name,
            "last_name": last_name,
            "email": f"{first_name}{last_name}{randint(0,9)}@{get_random_item_from(email_providers)}.com",
            "phone": randint(1000000000, 9999999999),
            "type": randint(0, 2),
            "zip": generate_fake_zip(),
            "city": get_random_item_from(bc_cities),
            "province": "BC",
            "building_number": randint(0, 99999),
            "unit_number": randint(0, 1000),
            "street_name": get_random_item_from(fake_street_names),
            "card_number": str(randint(1000000000000000, 9999999999999999)),
            "expiration_date": randint(1000, 5000),
            "bank_name": get_random_item_from(bank_names),
            "card_type": get_random_item_from(debit_credit),
            "payment_system": get_random_item_from(visa_mastercard)
        }
        register_user(fake_user_details)


def populate_register_speeder():
    for i in range(5):
        try:
            insert_row("Speeder", insert_speeder_query, (i, 2, 123, 49))
        except:
            pass

def populate_register_restaurant():
    for i in range(len(restaurant_names)):

        register_restaurant_detail = {
            "restaurant_manager_email": get_random_user_email_from_db(),
            "restaurant_name": restaurant_names[i],
            "cuisine": get_random_item_from(list_of_cuisine),
        }
        register_restaurant(register_restaurant_detail)

def populate_insert_restaurant_item():
    for i in range(50):
        item_details = {
            "item_name": get_random_item_from(list_of_dishes),
            "restaurant_name": get_random_restaurant_from_db(),
            "price": randint(1, 30),
            'user_email': get_random_user_email_from_db()
        }
        insert_restaurant_item(item_details)

def populate_place_order():
    for i in range(10):
        restaurant_name = get_random_restaurant_from_db()
        example_order = {
            'tip': randint(0, 20),
            'status': 0,
            'special_instructions': ["None", "please Include utensils"][randint(0, 1)],
            'consumer_email': get_random_user_email_from_db(),
            'restaurant_name': restaurant_name,
            'item_name': get_random_item_from_restaurant(restaurant_name)
        }
        place_order(example_order)

# TODO: Rithik
def populate_rate_restaurant():
    # Refer to this
    # CREATE TABLE UserToUser_Reviews (
    #     user_id_ratable INTEGER,
    #     user_id_consumer INTEGER NOT NULL,
    #     rating_time TIMESTAMP,
    #     value  INTEGER NOT NULL,
    #     review TEXT,
    #     PRIMARY KEY (user_id_ratable, user_id_consumer, rating_time),
    #     FOREIGN KEY (User_id_consumer) REFERENCES User(user_id),
    #     CHECK (value >= 1 AND value <= 5)

    for i in range(10):
        restaurant_name1 = get_random_restaurant_from_db()
        rest_id1 = get_restaurant_id_by_name(restaurant_name1)
        example_rating1 = {
            'restaurant': rest_id1,
            'cons_email1': get_random_user_email_from_db(),
            'rating_time': 0,  # not sure how to get a random time stamp,
            'value': randint(1, 5),
            'review': ["None", "Very tasty food, speedy delivery"]  # not sure if this is how TEXT data type is done
        }
        rate_restaurant(example_rating1)
    # pass


def insert_random_data():
    populate_register_user()
    populate_register_speeder()
    populate_register_restaurant()
    populate_insert_restaurant_item()
    populate_place_order()
    populate_rate_restaurant()


if __name__ == "__main__":
    """
    The order of which we want to populate the tables
    """
    insert_random_data()
