# from fake_values import fake_emails, fake_names
from db_client import cursor, db
from datetime import date, datetime
from random import randint, randrange
from queries.insert_queries import *

from utils.helper import delete_all_rows_from_database, list_of_tables

fake_zip = "V6R1Y5"
# user_id, address_id, order_id are autoincremented, doing sample data for one user/address/order only
# auto-increment starts with 1
user_id, address_id, order_id = 1, 1, 1

def insert_test(query_name, insert_query, insert_tuple):
    cursor.execute(insert_query, insert_tuple)
    print(f"{query_name} inserted successfully with values {insert_tuple}")
    db.commit()


def insert_sample_rows():
    delete_all_rows_from_database(list_of_tables)

    insert_test("Card BIN", insert_card_bin_query,
                (123456, "CIBC", 0, "Visa"))

    # must convert input to lower case
    insert_test("Restaurant Parent", insert_restaurant_parent_query,
                ("McDonalds", "Fast Food"))

    insert_test("City", insert_city_query,
                ("Vancouver", "British Columbia"))

    # must convert city to lower case since duplicate cities with the same name could arise
    # and because city_name is a primary key
    insert_test("Zip", insert_zip_query, (fake_zip, "vancouver"))

    insert_test("User", insert_user_query,
                ("tomi","Liu", "tomi@gmail.com", "7786966999", 0))

    insert_test("User to User reviews", insert_user_to_user_reviews_query,
                (user_id, user_id, datetime.now(), 5, "very tasty food!!"))

    insert_test("User Address", insert_user_address_query,
                (user_id, fake_zip, 33, 12, "Cambie st"))

    insert_test("Speeder", insert_speeder_query, (user_id, 2, 123, 49))

    # must convert input to lower case
    insert_test("Restaurant", insert_restaurant_query, (user_id, "McDonalds"))

    insert_test("Card All", insert_card_all_query, (123456, 1111111111,
                datetime.now().month + datetime.now().year, fake_zip, user_id))

    insert_test("Item", insert_item_query, ("chicken nuggets", user_id, 6.9))

    # order id?
    # remember to consider status for future
    insert_test("Order", insert_order_query,
               (1.3, 2, datetime.now(), "Please include utensils", user_id, user_id, user_id))

    insert_test("Order to Item", insert_order_to_item_query,
                (order_id, user_id, "chicken nuggets"))


if __name__ == "__main__":
    insert_sample_rows()
