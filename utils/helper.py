"""
misc helper function
"""
import string
from db_client import cursor
from random import choice, randint

list_of_tables = [
    "Card_BIN",
    "RestaurantParent",
    "City ",
    "Zip ",
    "User",
    "User_Address ",
    "UserToUser_Reviews",
    "Speeder ",
    "Restaurant",
    "Card_All",
    "Item ",
    "_Order ",
    "OrderToItem ",
]


def get_random_item_from_restaurant(restaurant_name):
    restaurant_id = get_restaurant_id_by_name(restaurant_name)
    cursor.execute(f"select item_name from Item WHERE restaurant_id = '{restaurant_id}' ORDER BY RAND() ")
    myresult = cursor.fetchone()
    return myresult[0]

def get_random_user_email_from_db():
    cursor.execute("select email from User ORDER BY RAND()")
    myresult = cursor.fetchall()
    return myresult[0][0]

def get_random_restaurant_from_db():
    cursor.execute("select restaurant_name from Restaurant ORDER BY RAND()")
    myresult = cursor.fetchall()
    return myresult[0][0]



def split_card_number(card_number):
    return [card_number[:6], card_number[6:]]

def get_user_id_by_email(email):
    cursor.execute(f"SELECT user_id FROM User WHERE email = '{email}'")
    myresult = cursor.fetchall()
    for x in myresult:
        return x[0]

def get_restaurant_id_by_name(restaurant_name):
    cursor.execute(f"SELECT restaurant_id FROM Restaurant WHERE restaurant_name = '{restaurant_name}'")
    myresult = cursor.fetchall()
    return myresult[0][0]

def get_random_speeder_id_from_db():
    cursor.execute("select speeder_id from Speeder ORDER BY RAND()")
    myresult = cursor.fetchall()
    return myresult[0][0]

def value_exist_in_column(table, column, value):
    """
    returns true if 'value' exists in 'column' from 'table'
    """
    cursor.execute(f"select * from {table} where {column} = '{value}'")
    myresult = cursor.fetchall()
    return len(myresult) > 0



def get_random_phone_number():
    # returns a random 10 digit phone number
    return randint(1000000000, 9999999999)

def generate_fake_zip():
    zip = choice(string.ascii_letters) + str(randint(0, 9)) + choice(string.ascii_letters) + \
        str(randint(0, 9)) + choice(string.ascii_letters) + str(randint(0, 9))
    return zip.upper()


def get_random_item_from(item_list):
    # returns a random item from a given list
    return item_list[randint(0, len(item_list)-1)]

def get_random_user_type():
    return randint(0, 3)

def delete_all_rows_from_table(table_name):
    cursor.execute(f"DELETE FROM {table_name};")


def delete_all_rows_from_database(database_tables):
    for table in database_tables:
        delete_all_rows_from_table(table)

def delete_all_tables():
    cursor.execute("DROP DATABASE testdatabase;")
    cursor.execute("CREATE DATABASE testdatabase;")
    cursor.execute("use testdatabase;")