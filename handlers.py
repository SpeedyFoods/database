from db_client import db, cursor
from queries.insert_queries import *


def insert_row(query_name, insert_query, insert_tuple):
    cursor.execute(insert_query, insert_tuple)
    print(f"{query_name} inserted successfully")
    db.commit()

def split_card_number(card_number):
    return [card_number[0:5], card_number[5:]]

def get_user_id_by_email(email):
    cursor.execute(f"SELECT user_id FROM User WHERE email = '{email}'")
    myresult = cursor.fetchall()
    for x in myresult:
        return x[0]

def value_exist_in_column(table, column, value):
    """
    returns true if 'value' exists in 'column' from 'table'
    """
    cursor.execute(f"select * from {table} where {column} = '{value}'")
    myresult = cursor.fetchall()
    return len(myresult) > 0


def register_user(user_detail):
    # we should do data validation. right now im able to insert multiple users with the same info. Myabe change some values to UNIQUE?
    res = {}
    res['success'] = False
    res['error'] = "no errors"

    try:
        # INSERT USER
        insert_row("User", insert_user_query, (user_detail['first_name'], 
            user_detail['last_name'], user_detail['email'], user_detail['phone'], user_detail['type']))

        # query user_id that was just inserted to be used later
        user_id = get_user_id_by_email(user_detail['email'])

        city = user_detail['city'].lower()
        if(not value_exist_in_column('City', 'city_name', city)):
            insert_row('City', insert_city_query, (city, user_detail['province'] ))

        # print("---------------- ZIP")
        # validation
        # if zip no in in column, insert it:
        if (not value_exist_in_column("Zip", 'zip', user_detail['zip'])):
            insert_row("Zip", insert_zip_query, (user_detail['zip'], user_detail['city']))

        # print("---------------- ADDRESS")
        # INSERT ADDRESS
        insert_row("Address", insert_user_address_query, (user_id, user_detail['zip'], user_detail['building_number'], 
            user_detail['unit_number'], user_detail['street_name']))

        # remember to validate cardnumber has 16 digits
        [card_number_6,card_number_rest] = split_card_number(user_detail['card_number'])

        # print("---------------- CARDBIN")
        # INSERT CARD BIN
        # validation:
        if (not value_exist_in_column('Card_BIN', 'card_number_6', card_number_6)):
            insert_row("Card_BIN", insert_card_bin_query, (card_number_6, 
                user_detail['bank_name'], user_detail['card_type'],
                user_detail['payment_system']))

        # print("---------------- Card_ALL")
        # INSERT CARD ALL
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

# TODO:
def register_restaurant():
    pass


def place_order():
    pass


def rate_restaurant():
    pass

# Select queries here?

def view_users():
    pass


def view_restaurants():
    pass

def view_restaurant_items():
    pass