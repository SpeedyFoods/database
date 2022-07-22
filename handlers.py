from db_client import db, cursor
from queries.insert_queries import *


def insert_row(query_name, insert_query, insert_tuple):
    cursor.execute(insert_query, insert_tuple)
    print(f"{query_name} inserted successfully")
    db.commit()

def split_card_number(card_number):
    pass

def register_user(user_detail):
    # should split card number into 2 parts, 6 digits for BIN and rest for 'rest'

    insert_row("User", insert_user_query, (user_detail['first_name'], 
        user_detail['last_name'], user_detail['email'], user_detail['phone'], user_detail['type']))

    insert_row("Address", insert_user_address_query, (user_detail['user_id'], user_detail['zip'], user_detail['building_number'], 
        user_detail['unit_number'], user_detail['street_name']))

    [card_number_6,card_number_rest] = split_card_number(user_detail['card_number'])
    insert_row("Card_All", insert_card_all_query, (card_number_6, 
        card_number_rest, user_detail['expiration_date'], 
        user_detail['zip']))

    insert_row("Card_BIN", insert_card_bin_query, (user_detail['card_number_6'], 
        user_detail['bank_name'], user_detail['card_type'], 
        user_detail['payment_system']))
    
    

def register_restaurant():
    pass


def place_order():
    pass


def rate_restaurant():
    pass
