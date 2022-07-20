from db_client import cursor
from random import randint

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