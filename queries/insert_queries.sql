INSERT INTO Users (
	user_id, 
	name, 
	email, 
	phone, 
	type
);

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
);

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date, 
	zip,
);


INSERT INTO User_Address (
	address_id,
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name,
);

INSERT INTO Zip (
	zip,
	city_name,
);

INSERT INTO City (
	city_name,
	province_name
);

INSERT INTO UserToUser_Reviews (
	user_id_ratable, 
	user_id_consumer, 
	rating_time,
	value,
	review,
);

INSERT INTO Speeder (
	speeder_id,
	transit, 
	current_long, 
	current_lat,
);

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

INSERT INTO Restaurant (
	restaurant_name,
	restaurant_id,
	restaurant_id,
);

INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price,
);


INSERT INTO OrderToItem (
	order_id,
	restaurant_id,
	item_name,
);
