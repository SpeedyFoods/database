insert_user_query = """
INSERT INTO Users (
	name, 
	email, 
	phone, 
	type
)
VALUES (%s, %s, %s, %s) 
# """

inser_card_bin_query = """
INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (%s, %s, %s, %s)
"""

insert_card_all_query = """
# INSERT INTO Card_All (
# 	card_number_6, 
# 	card_number_rest,
# 	expiration_date, 
# 	zip,
# )
VALUES (%s, %s, %s, %s)
"""


insert_user_address_query = """
INSERT INTO User_Address (
	address_id,
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name,
VALUES (%s, %s, %s, %s, %s, %s)
);
"""

insert_zip_query = """
INSERT INTO Zip (
	zip,
	city_name,
)
VALUES (%s, %s)
"""

insert_city_query = """
INSERT INTO City (
	city_name,
	province_name
)
VALUES (%s, %s)
"""

insert_user_to_user_reviews_query = """
INSERT INTO UserToUser_Reviews (
	user_id_ratable, 
	user_id_consumer, 
	rating_time,
	value,
	review,
)
VALUES (%s, %s, %s, %s, %s)
"""

insert_speeder_query = """
INSERT INTO Speeder (
	speeder_id,
	transit, 
	current_long, 
	current_lat,
)
VALUES (%s, %s, %s, %s)
"""

insert_order_query = """
INSERT INTO Order (
	order_id,
	tip,
	status, 
	order_time, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id,
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

insert_restaurant_query = """
INSERT INTO Restaurant (
	restaurant_name,
	restaurant_id,
	restaurant_id,
)
VALUES (%s, %s, %s)
"""

insert_restaurant_parent_query = """
INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
VALUES (%s, %s)
"""

insert_item_query = """
INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price,
)
VALUES (%s, %s, %s)
"""


insert_order_to_item_query = """
INSERT INTO OrderToItem (
	order_id,
	restaurant_id,
	item_name,
)
VALUES (%s, %s, %s)
"""