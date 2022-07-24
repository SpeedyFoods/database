"""
This file is a script that helps us populate all data(rows) to all of our Tables. 
a file that helps us insert bulk data to our database using our main funcitons from handlers.py
"""

from utils.fake_values import fake_names, email_providers, bc_cities, fake_street_names, bank_names, debit_credit, visa_mastercard
from random import randint, choice
import string
from handlers import register_user
from utils.helper import generate_fake_zip, get_random_item_from

# discuss

def populate_register_user():
    """
    insert 10 random user data information to the tables User, Address, Zip, Card_BIN, Card_All
    """
    for i in range(10):
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


# discuss
# TODO:
def populate_register_restaurant():
    pass

# TODO: might not need to do this
def populate_place_order():
    pass

# TODO:
def populate_rate_restaurant():
    pass


def insert_random_data():

    populate_register_user()
    populate_register_restaurant()
    populate_place_order()
    populate_rate_restaurant()
if __name__ == "__main__":
    """
    The order of which we want to populate the tables
    """
    insert_random_data()