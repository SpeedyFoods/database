# from fake_values import fake_emails, fake_names
import sys
sys.path.append('..')
from queries.insert_queries import *
from random import randint, randrange
import sys
from datetime import date, datetime
from db_client import cursor


from numpy import insert


fake_zip = "V6R1Y5"


def insert_test(query_name, insert_query, insert_tuple):
    cursor.execute(insert_query, insert_tuple)
    print(f"{query_name} inserted successfully")


def get_random_phone_number():
    # returns a random 10 digit phone number
    return randint(1000000000, 9999999999)

def get_random_user_type():
    return randint(0, 3)

def delete_all_rows_from(table_name):
    cursor.execute(f"DELETE FROM {table_name};")


"""
CREATE TABLE User (
    user_id int auto increment,
    name char(20) NOT NULL,
    email char(30) NOT NULL,
    phone char(20) NOT NULL,
    type int NOT NULL,
    PRIMARY KEY (user_id),
    CHECK (type <= 2 AND type >= 0)
);

"""
insert_test("User", insert_user_query,
            ("tomi", "tomi@gmail.com", "7786966999", 0))


"""
CREATE TABLE Card_BIN (
    card_number_6 char(6),
    bank_name char(50) NOT NULL,
    card_type char(20) NOT NULL,
    payment_system char(30) NOT NULL,
    PRIMARY KEY (card_number_6)
);
"""
insert_test("Card BIN", insert_card_bin_query,
            (123456, "CIBC", "CREDIT", "VISA"))


"""
INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date, 
	zip,
)
"""
insert_test("Card All", insert_card_all_query, (123456, 1111111111, datetime.now().month + datetime.now().year, fake_zip))

"""
INSERT INTO Zip (
	zip,
	city_name,
);
"""
# must convert city to lower case since duplicate cities with the same name could arise
# and because city_name is a primary key
insert_test("Zip", insert_zip_query, (fake_zip, "vancouver"))

"""
INSERT INTO City (
	city_name,
	province_name
);
"""
insert_test("City", insert_city_query, ("vancouver", "british columbia"))

"""
INSERT INTO UserToUser_Reviews (
	user_id_ratable,
	user_id_consumer,
	rating_time,
	value,
	review,
);
"""
# not sure how to insert
insert_test("User to User reviews", insert_user_to_user_reviews_query, (0, 0, datetime.now(), 5, "very tasty food!!"))


"""
INSERT INTO Speeder (
	speeder_id,
	transit,
	current_long,
	current_lat,
);
"""
# speeder id?
insert_test("Speeder", insert_speeder_query, (0, 0, 123, 49))


"""
INSERT INTO Order (
	order_id,
	tip,
	status,
	order_time,
	special_instructions,
	consumer_id,
	restaurant_id,
	speeder_id,
);
"""
# order id?
# remember to consider status for future
insert_test("Order", insert_order_query, (0,2, 0, datetime().now(), "Please include utensils", 0, 0, 0))


"""
INSERT INTO Restaurant (
	restaurant_name,
	restaurant_id,
);
"""
# must convert input to lower case
insert_test("Restaurant", insert_restaurant_query, ("McDonalds", 0))


"""
INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
"""
# not sure how to insert this
# must convert input to lower case
insert_test("Restaurant Parent", insert_restaurant_parent_query, ("McDonalds", "Fast Food"))

"""
INSERT INTO Item (
	item_name,
	restaurant_id ,
	price,
);
"""
insert_test("Item", insert_item_query, ("chicken nuggets", 0, 6.9))


"""
INSERT INTO OrderToItem (
	order_id,
	restaurant_id,
	item_name,
);
"""
insert_test("Order to Item", insert_order_to_item_query, (0, 0, "chicken nuggets"))
