# from fake_values import fake_emails, fake_names
from db_client import cursor, db
from datetime import date, datetime
from random import randint, randrange
from queries.insert_queries import *

from utils import delete_all_rows_from_database, list_of_tables

fake_zip = "V6R1Y5"


def insert_test(query_name, insert_query, insert_tuple):
    cursor.execute(insert_query, insert_tuple)
    print(f"{query_name} inserted successfully")
    db.commit()


def insert_sample_rows():
    delete_all_rows_from_database(list_of_tables)

    insert_test("Card BIN", insert_card_bin_query,
                (123456, "CIBC", "CREDIT", "VISA"))

    # not sure how to insert this
    # must convert input to lower case
    insert_test("Restaurant Parent", insert_restaurant_parent_query,
                ("McDonalds", "Fast Food"))

    insert_test("City", insert_city_query,
                ("vancouver", "british columbia"))

    # must convert city to lower case since duplicate cities with the same name could arise
    # and because city_name is a primary key
    insert_test("Zip", insert_zip_query, (fake_zip, "vancouver"))

    insert_test("User", insert_user_query,
                ("tomi", "tomi@gmail.com", "7786966999", 0))

    # insert does not work because of foreign key constraints
    # insert_test("User to User reviews", insert_user_to_user_reviews_query,
    # 			(0, 0, datetime.now(), 5, "very tasty food!!"))

    # cannot insert due to foreign key constraint
    # insert_test("User Address", insert_user_address_query,
    # 			(0, fake_zip, 0, 0, "Cambie st"))

    # speeder id?
    insert_test("Speeder", insert_speeder_query, (0, 0, 123, 49))

    # must convert input to lower case
    insert_test("Restaurant", insert_restaurant_query, ("McDonalds", 0))

    # cannot update because of foreign key constraint
    # insert_test("Card All", insert_card_all_query, (123456, 1111111111,
    # 			datetime.now().month + datetime.now().year, fake_zip))

    # cannot update because of foreign key constraint
    # insert_test("Item", insert_item_query, ("chicken nuggets", 0, 6.9))

    # order id?
    # remember to consider status for future
    # cannot update because of foreign key constraint
    # insert_test("Order", insert_order_query,
    # 			(2, 0, datetime.now(), "Please include utensils", 0, 0, 0))

    # cannot update because of foreign key constraint
    # insert_test("Order to Item", insert_order_to_item_query,
    # 			(0, 0, "chicken nuggets"))


if __name__ == "__main__":
    insert_sample_rows()
