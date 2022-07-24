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