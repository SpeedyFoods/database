-- DROP DATABASE testdatabase;
CREATE DATABASE testdatabase;
use testdatabase;
show tables;

CREATE TABLE Card_BIN (
    card_number_6 CHAR(6),
    bank_name CHAR(50) NOT NULL,
    card_type INT NOT NULL,
    payment_system CHAR(30) NOT NULL,
    PRIMARY KEY (card_number_6),
    CHECK (card_type >= 0 AND card_type <= 1)
);

CREATE TABLE RestaurantParent (
    restaurant_name CHAR(50) NOT NULL,
    cuisine CHAR(20),
    PRIMARY KEY (restaurant_name)
);

CREATE TABLE City (
    city_name CHAR(25),
    province_name CHAR(25),
    PRIMARY KEY (city_name)
);

CREATE TABLE Zip (
    zip CHAR(6),
    city_name CHAR(30) NOT NULL,
    PRIMARY KEY (zip),
    FOREIGN KEY (city_name) REFERENCES City(city_name)
);

CREATE TABLE User (
    user_id int AUTO_INCREMENT,
    first_name CHAR(20) NOT NULL,
    last_name CHAR(20) NOT NULL,
    email CHAR(30) NOT NULL UNIQUE,
    phone CHAR(20) NOT NULL,
    type int NOT NULL,
    PRIMARY KEY (user_id),
    CHECK (type <= 2 AND type >= 0)
);

CREATE TABLE User_Address (
    address_id INTEGER AUTO_INCREMENT,
    user_id INTEGER, 
    zip CHAR(6), 
    building_number INTEGER, 
    unit_number INTEGER, 
    street_name CHAR(50),
    PRIMARY KEY (address_id),
    FOREIGN KEY (zip) REFERENCES Zip(zip),
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE
);

CREATE TABLE UserToUser_Reviews (
    user_id_ratable INTEGER, 
    user_id_consumer INTEGER NOT NULL, 
    rating_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    value  INTEGER NOT NULL,
    review TEXT,
    PRIMARY KEY (user_id_ratable, user_id_consumer, rating_time),
    FOREIGN KEY (User_id_consumer) REFERENCES User(user_id) ON DELETE CASCADE,
    CHECK (value >= 1 AND value <= 5)
);

CREATE TABLE Speeder (
    speeder_id INTEGER,
    transit INTEGER NOT NULL, 
    current_long FLOAT NOT NULL, 
    current_lat FLOAT NOT NULL,
    PRIMARY KEY (speeder_id),
    FOREIGN KEY (speeder_id) REFERENCES User(user_id) ON DELETE CASCADE,
    CHECK (transit >= 0 AND transit <= 2),
    CHECK (current_long >= -180 AND current_long <= 180), 
    CHECK (current_lat >= -90 AND current_lat <= 90)
);

CREATE TABLE Restaurant (
    restaurant_id INTEGER,
    restaurant_name CHAR(50) UNIQUE,
    PRIMARY KEY (restaurant_id),
    FOREIGN KEY (restaurant_name) References RestaurantParent(restaurant_name),
    FOREIGN KEY (restaurant_id) REFERENCES User(user_id) ON DELETE CASCADE
);

CREATE TABLE Card_All (
    card_number_6 CHAR(6), 
    card_number_rest CHAR(10),
    expiration_date DATE NOT NULL, 
    zip CHAR(6) NOT NULL,
    user_id INTEGER NOT NULL, 
    PRIMARY KEY (card_number_6, card_number_rest),
    FOREIGN KEY (zip) REFERENCES Zip(zip),
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE,
    FOREIGN KEY (card_number_6) REFERENCES Card_BIN(card_number_6)
);

CREATE TABLE Item (
    item_name CHAR(20), 
    restaurant_id INTEGER,
    price FLOAT NOT NULL,
    PRIMARY KEY (item_name, restaurant_id),
    FOREIGN KEY (restaurant_id) REFERENCES Restaurant(restaurant_id) ON DELETE CASCADE
);

CREATE TABLE _Order (
    order_id INTEGER AUTO_INCREMENT,
    tip FLOAT NOT NULL,
    status INTEGER NOT NULL,
    order_time TIMESTAMP NOT NULL, 
    special_instructions CHAR(250), 
    consumer_id INTEGER, 
    restaurant_id INTEGER, 
    speeder_id INTEGER,
    PRIMARY KEY (order_id),
    FOREIGN KEY (consumer_id) REFERENCES User(user_id) ON DELETE CASCADE,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurant(restaurant_id) ON DELETE CASCADE,
    FOREIGN KEY (speeder_id) REFERENCES Speeder(speeder_id) ON DELETE CASCADE,
    CHECK (status <= 3 AND status >= 0)
);

CREATE TABLE OrderToItem (
    order_id INTEGER,
    restaurant_id INTEGER,
    item_name CHAR(20),
    PRIMARY KEY (order_id, restaurant_id, item_name),
    FOREIGN KEY (order_id) REFERENCES _Order(order_id) ON DELETE CASCADE,
    FOREIGN KEY (item_name, restaurant_id) REFERENCES Item(item_name, restaurant_id) ON DELETE CASCADE
);



INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Annabel', 'Downs', 'AnnabelDowns6@hotmail.com', 1346599700, 2) 
 ;

INSERT INTO City (
	city_name,
	province_name
)
VALUES ('maple ridge', 'BC')
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('A9K9H5', 'MAPLE RIDGE')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (1, 'A9K9H5', 78270, 793, 'Christopher Ridge')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (429458, 'Desjardins Group', 'debit', 'visa')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (429458, 3673231878, 1432, 'A9K9H5', 1)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('King', 'Frank', 'KingFrank3@outlook.com', 9324886303, 0) 
 ;

INSERT INTO City (
	city_name,
	province_name
)
VALUES ('port coquitlam', 'BC')
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('W4S3M3', 'PORT COQUITLAM')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (2, 'W4S3M3', 80433, 825, 'Coopers Circus')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (296329, 'Toronto-Dominion Bank', 'debit', 'mastercard')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (296329, 3051576050, 4051, 'W4S3M3', 2)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Leonard', 'Ray', 'LeonardRay6@gmail.com', 5464805079, 1) 
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('K1C2R9', 'MAPLE RIDGE')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (3, 'K1C2R9', 99855, 699, 'Coopers Circus')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (604705, 'CIBC', 'debit', 'mastercard')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (604705, 4875218697, 1205, 'K1C2R9', 3)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Brianna', 'Wells', 'BriannaWells1@outlook.com', 5584497320, 0) 
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('C5N6K0', 'MAPLE RIDGE')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (4, 'C5N6K0', 49914, 985, 'Copley Place')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (250295, 'Royal Bank of Canada', 'debit', 'mastercard')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (250295, 7462654342, 1666, 'C5N6K0', 4)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Jazlynn', 'Bauer', 'JazlynnBauer3@outlook.com', 6477606880, 1) 
 ;

INSERT INTO City (
	city_name,
	province_name
)
VALUES ('vancouver', 'BC')
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('D7Q8H5', 'VANCOUVER')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (5, 'D7Q8H5', 7478, 157, 'Coopers Circus')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (800898, 'CIBC', 'debit', 'mastercard')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (800898, 9896344789, 1135, 'D7Q8H5', 5)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Marcelo', 'Hubbard', 'MarceloHubbard7@yahoo.com', 3571954712, 2) 
 ;

INSERT INTO City (
	city_name,
	province_name
)
VALUES ('burnaby', 'BC')
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('C8E4E9', 'BURNABY')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (6, 'C8E4E9', 16607, 171, 'Copley Place')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (712201, 'Royal Bank of Canada', 'credit', 'visa')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (712201, 1265811323, 1637, 'C8E4E9', 6)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Jaidyn', 'Spears', 'JaidynSpears0@hotmail.com', 5219063808, 2) 
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('V7J9T2', 'MAPLE RIDGE')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (7, 'V7J9T2', 39583, 637, 'Copley Place')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (910781, 'Royal Bank of Canada', 'credit', 'visa')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (910781, 0237024738, 2488, 'V7J9T2', 7)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Ivy', 'Graham', 'IvyGraham1@outlook.com', 1612343608, 1) 
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('I3I0J3', 'VANCOUVER')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (8, 'I3I0J3', 48445, 591, 'Carfin Drive')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (998279, 'Toronto-Dominion Bank', 'credit', 'mastercard')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (998279, 7561886199, 2047, 'I3I0J3', 8)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Manuel', 'Li', 'ManuelLi4@gmail.com', 8081255811, 2) 
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('O2D6I5', 'VANCOUVER')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (9, 'O2D6I5', 39968, 418, 'Carfin Drive')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (526470, 'HSBC', 'credit', 'mastercard')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (526470, 0417641377, 2903, 'O2D6I5', 9)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Kenzie', 'West', 'KenzieWest2@gmail.com', 4136017496, 1) 
 ;

INSERT INTO City (
	city_name,
	province_name
)
VALUES ('surrey', 'BC')
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('P4P8E9', 'SURREY')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (10, 'P4P8E9', 84417, 811, 'Carlisle Fold')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (993201, 'Royal Bank of Canada', 'credit', 'mastercard')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (993201, 5250954047, 4774, 'P4P8E9', 10)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Raelynn', 'Mccullough', 'RaelynnMccullough7@outlook.com', 7273566322, 0) 
 ;

INSERT INTO City (
	city_name,
	province_name
)
VALUES ('coquitlam', 'BC')
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('O7U1A7', 'COQUITLAM')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (11, 'O7U1A7', 22996, 340, 'Carisbrooke Gate')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (687246, 'Royal Bank of Canada', 'debit', 'mastercard')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (687246, 5572465350, 4937, 'O7U1A7', 11)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Kamden', 'Carney', 'KamdenCarney0@outlook.com', 5857598098, 1) 
 ;

INSERT INTO City (
	city_name,
	province_name
)
VALUES ('new westminster', 'BC')
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('E3P8A0', 'NEW WESTMINSTER')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (12, 'E3P8A0', 27816, 777, 'Cameron Heights')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (536012, 'Desjardins Group', 'credit', 'visa')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (536012, 6666091141, 1356, 'E3P8A0', 12)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Angie', 'Riley', 'AngieRiley8@outlook.com', 9783650491, 2) 
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('P9E0R5', 'COQUITLAM')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (13, 'P9E0R5', 73386, 259, 'Cardigan Ridgeway')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (410228, 'National Bank', 'debit', 'visa')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (410228, 4412450243, 3192, 'P9E0R5', 13)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Francis', 'Floyd', 'FrancisFloyd2@gmail.com', 4759030626, 0) 
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('A2F7V9', 'PORT COQUITLAM')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (14, 'A2F7V9', 853, 745, 'Carfin Drive')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (582043, 'Desjardins Group', 'credit', 'visa')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (582043, 1712737336, 4827, 'A2F7V9', 14)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Jayvon', 'Shea', 'JayvonShea3@gmail.com', 4290219093, 2) 
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('H4V3B3', 'SURREY')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (15, 'H4V3B3', 42222, 266, 'Cardigan Ridgeway')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (681374, 'HSBC', 'debit', 'mastercard')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (681374, 7701728982, 1062, 'H4V3B3', 15)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Jayvon', 'Shea', 'JayvonShea0@hotmail.com', 1538105325, 2) 
 ;

INSERT INTO City (
	city_name,
	province_name
)
VALUES ('port moody', 'BC')
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('I4K3H7', 'PORT MOODY')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (16, 'I4K3H7', 54567, 914, 'Coopers Circus')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (218792, 'Toronto-Dominion Bank', 'credit', 'mastercard')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (218792, 4819326594, 1202, 'I4K3H7', 16)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Rayna', 'Delgado', 'RaynaDelgado1@outlook.com', 9732670738, 2) 
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('F1R6S6', 'COQUITLAM')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (17, 'F1R6S6', 47363, 418, 'Cardigan Ridgeway')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (951704, 'Bank of Nova Scotia', 'debit', 'visa')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (951704, 3949434741, 4461, 'F1R6S6', 17)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Brian', 'Dalton', 'BrianDalton2@gmail.com', 3576006017, 1) 
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('V7D6Y9', 'BURNABY')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (18, 'V7D6Y9', 40920, 789, 'Coopers Circus')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (632889, 'Desjardins Group', 'credit', 'visa')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (632889, 3130124818, 2622, 'V7D6Y9', 18)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Junior', 'Carson', 'JuniorCarson7@yahoo.com', 8810902483, 2) 
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('S8I5K6', 'VANCOUVER')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (19, 'S8I5K6', 89724, 984, 'Christopher Ridge')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (921704, 'Bank of Montreal', 'debit', 'mastercard')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (921704, 4547836357, 4859, 'S8I5K6', 19)
 ;

INSERT INTO User (
	first_name, 
	last_name, 
	email, 
	phone, 
	type
)
VALUES ('Neil', 'Haney', 'NeilHaney2@gmail.com', 1262345595, 1) 
 ;

INSERT INTO Zip (
	zip,
	city_name
)
VALUES ('C4D9C2', 'NEW WESTMINSTER')
 ;

INSERT INTO User_Address (
	user_id, 
	zip,
	building_number, 
	unit_number, 
	street_name
)
VALUES (20, 'C4D9C2', 71049, 40, 'Cameron Heights')
 ;

INSERT INTO Card_BIN (
	card_number_6,
	bank_name,
	card_type, 
	payment_system
)
VALUES (369578, 'Royal Bank of Canada', 'debit', 'mastercard')
 ;

INSERT INTO Card_All (
	card_number_6, 
	card_number_rest,
	expiration_date,
	zip,
	user_id
)
VALUES (369578, 5606524657, 3370, 'C4D9C2', 20)
 ;

INSERT INTO Speeder (
	speeder_id,
	transit, 
	current_long, 
	current_lat
)
VALUES (1, 2, 123, 49)
 ;

INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
VALUES ('McDonalds', 'American')
 ;

INSERT INTO Restaurant (
	restaurant_id,
	restaurant_name
)
VALUES (17, 'McDonalds')
 ;

INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
VALUES ('Chick-fil-A', 'Asian')
 ;

INSERT INTO Restaurant (
	restaurant_id,
	restaurant_name
)
VALUES (7, 'Chick-fil-A')
 ;

INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
VALUES ('Wendys', 'American')
 ;

INSERT INTO Restaurant (
	restaurant_id,
	restaurant_name
)
VALUES (15, 'Wendys')
 ;

INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
VALUES ('Dunkin', 'Indian')
 ;

INSERT INTO Restaurant (
	restaurant_id,
	restaurant_name
)
VALUES (11, 'Dunkin')
 ;

INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
VALUES ('Burger King', 'Indian')
 ;

INSERT INTO Restaurant (
	restaurant_id,
	restaurant_name
)
VALUES (18, 'Burger King')
 ;

INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
VALUES ('Subway', 'Asian')
 ;

INSERT INTO Restaurant (
	restaurant_id,
	restaurant_name
)
VALUES (20, 'Subway')
 ;

INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
VALUES ('Chipotle Mexican Grill', 'Asian')
 ;

INSERT INTO Restaurant (
	restaurant_id,
	restaurant_name
)
VALUES (19, 'Chipotle Mexican Grill')
 ;

INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
VALUES ('Panera Bread', 'European')
 ;

INSERT INTO Restaurant (
	restaurant_id,
	restaurant_name
)
VALUES (14, 'Panera Bread')
 ;

INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
VALUES ('Pizza-Hut', 'European')
 ;

INSERT INTO Restaurant (
	restaurant_id,
	restaurant_name
)
VALUES (2, 'Pizza-Hut')
 ;

INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
VALUES ('KFC', 'Indian')
 ;

INSERT INTO Restaurant (
	restaurant_id,
	restaurant_name
)
VALUES (3, 'KFC')
 ;

INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
VALUES ('Popeyes', 'Japanese')
 ;

INSERT INTO Restaurant (
	restaurant_id,
	restaurant_name
)
VALUES (9, 'Popeyes')
 ;

INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
VALUES ('Panda Express', 'Indian')
 ;

INSERT INTO Restaurant (
	restaurant_id,
	restaurant_name
)
VALUES (13, 'Panda Express')
 ;

INSERT INTO RestaurantParent (
	restaurant_name,
	cuisine
)
VALUES ('Dairy Queen', 'Japanese')
 ;

INSERT INTO Restaurant (
	restaurant_id,
	restaurant_name
)
VALUES (10, 'Dairy Queen')
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Steamed Apple & Lavender Pheasant', 15, 24)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Stir-Fried Garlic & Lime Lamb', 20, 15)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Shallow-Fried Mint Mutton', 17, 14)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Cured Curry of Mammoth', 2, 30)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Seared Vinegar Yak', 20, 4)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Shallow-Fried Parsnip & Pear Mammoth', 14, 13)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Breaded Fennel & Lemon Turkey', 13, 24)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Dried Beets & Orange Rabbit', 11, 1)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Tenderized Dark Beer Mammoth', 2, 23)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Roasted Peppermint Turkey', 17, 21)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Grilled Truffles & Boar', 13, 27)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Seared Stew of Mutton', 18, 27)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Infused Salty & Sour Lamb', 11, 28)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Broasted White Wine Lamb', 15, 28)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Shallow-Fried Egg & Beet Yak', 10, 17)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Dried Olives & Mustard Rabbit', 17, 5)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Pressure-Cooked Ginger & Honey Yak', 15, 27)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Stir-Fried Apples & Walnut Venison', 3, 9)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Thermal-Cooked Chestnuts & Bear', 14, 8)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Basted Blackberry & Ginger Mammoth', 2, 3)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Roasted Peppermint Turkey', 7, 7)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Deep-Fried Honey & Nuts Mammoth', 17, 18)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Shallow-Fried Basil & Lime Turkey', 14, 24)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Poached Cranberry Venison', 2, 22)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Oven-Baked Red Whine Ostrich', 10, 16)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Shallow-Fried Egg & Beet Yak', 18, 15)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Fried Honey Quail', 18, 3)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Oven-Grilled Mushroom & Rosemary Mammoth', 20, 3)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Simmered Soy Quail', 9, 26)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Barbecued Mint & Mustard Beef', 20, 14)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Grilled Truffles & Boar', 9, 8)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Oven-Grilled Creamy Quail', 18, 29)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Dry-Roasted Parsnip & Pear Mutton', 14, 3)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Breaded Fennel & Lemon Turkey', 18, 28)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Infused Salty & Sour Lamb', 7, 12)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Oven-Baked Red Whine Ostrich', 3, 3)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Stir-Fried Apples & Walnut Venison', 14, 21)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Braised Fennel & Garlic Horse', 11, 23)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Deep-Fried Honey & Nuts Mammoth', 7, 29)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Basted Blueberry Pork', 17, 19)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Pickled Parsnip & Pear Beef', 14, 17)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Deep-Fried Honey & Nuts Mammoth', 9, 19)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Basted Blackberry & Ginger Mammoth', 11, 6)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Fire-Grilled Parsnip & Pear Beef', 14, 12)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Dried Olives & Mustard Rabbit', 3, 22)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Roasted Honey-Coated Mutton', 19, 14)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Baked Curry of Mutton', 11, 30)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Thermal-Cooked Chestnuts & Bear', 7, 17)
 ;

INSERT INTO Item (
	item_name, 
	restaurant_id ,
	price
)
VALUES ('Cooked Salty & Sour Ostrich', 7, 17)
 ;

INSERT INTO _Order (
	tip,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (13, 0, 'None', 8, 10, 1)
 ;

INSERT INTO OrderToItem (
	order_id,
	restaurant_id,
	item_name
)
VALUES (1, 10, 'Oven-Baked Red Whine')
 ;

INSERT INTO _Order (
	tip,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (2, 0, 'please Include utensils', 10, 15, 1)
 ;

INSERT INTO OrderToItem (
	order_id,
	restaurant_id,
	item_name
)
VALUES (2, 15, 'Steamed Apple & Lave')
 ;

INSERT INTO _Order (
	tip,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (9, 0, 'please Include utensils', 6, 19, 1)
 ;

INSERT INTO OrderToItem (
	order_id,
	restaurant_id,
	item_name
)
VALUES (3, 19, 'Roasted Honey-Coated')
 ;

INSERT INTO _Order (
	tip,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (13, 0, 'please Include utensils', 15, 15, 1)
 ;

INSERT INTO OrderToItem (
	order_id,
	restaurant_id,
	item_name
)
VALUES (4, 15, 'Pressure-Cooked Ging')
 ;

INSERT INTO _Order (
	tip,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (8, 0, 'None', 17, 13, 1)
 ;

INSERT INTO OrderToItem (
	order_id,
	restaurant_id,
	item_name
)
VALUES (5, 13, 'Breaded Fennel & Lem')
 ;

INSERT INTO _Order (
	tip,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (18, 0, 'please Include utensils', 14, 15, 1)
 ;

INSERT INTO OrderToItem (
	order_id,
	restaurant_id,
	item_name
)
VALUES (6, 15, 'Broasted White Wine')
 ;

INSERT INTO _Order (
	tip,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (13, 0, 'please Include utensils', 12, 19, 1)
 ;

INSERT INTO OrderToItem (
	order_id,
	restaurant_id,
	item_name
)
VALUES (7, 19, 'Roasted Honey-Coated')
 ;

INSERT INTO _Order (
	tip,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (13, 0, 'None', 4, 3, 1)
 ;

INSERT INTO OrderToItem (
	order_id,
	restaurant_id,
	item_name
)
VALUES (8, 3, 'Dried Olives & Musta')
 ;

INSERT INTO _Order (
	tip,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (8, 0, 'please Include utensils', 14, 15, 1)
 ;

INSERT INTO OrderToItem (
	order_id,
	restaurant_id,
	item_name
)
VALUES (9, 15, 'Broasted White Wine')
 ;

INSERT INTO _Order (
	tip,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (2, 0, 'please Include utensils', 1, 2, 1)
 ;

INSERT INTO OrderToItem (
	order_id,
	restaurant_id,
	item_name
)
VALUES (10, 2, 'Basted Blackberry &')
 ;

INSERT INTO UserToUser_Reviews (
	user_id_ratable, 
	user_id_consumer, 
	value,
	review
)
VALUES (17, 8, 3, 'Very tasty food, speedy delivery')
 ;

INSERT INTO UserToUser_Reviews (
	user_id_ratable, 
	user_id_consumer, 
	value,
	review
)
VALUES (13, 16, 1, 'Pretty Bad')
 ;

INSERT INTO UserToUser_Reviews (
	user_id_ratable, 
	user_id_consumer, 
	value,
	review
)
VALUES (3, 12, 2, 'Very tasty food, speedy delivery')
 ;

INSERT INTO UserToUser_Reviews (
	user_id_ratable, 
	user_id_consumer, 
	value,
	review
)
VALUES (17, 20, 1, 'Pretty Bad')
 ;

INSERT INTO UserToUser_Reviews (
	user_id_ratable, 
	user_id_consumer, 
	value,
	review
)
VALUES (2, 20, 1, 'Very tasty food, speedy delivery')
 ;

INSERT INTO UserToUser_Reviews (
	user_id_ratable, 
	user_id_consumer, 
	value,
	review
)
VALUES (17, 6, 2, 'Pretty Bad')
 ;

INSERT INTO UserToUser_Reviews (
	user_id_ratable, 
	user_id_consumer, 
	value,
	review
)
VALUES (17, 16, 3, 'Pretty Bad')
 ;

INSERT INTO UserToUser_Reviews (
	user_id_ratable, 
	user_id_consumer, 
	value,
	review
)
VALUES (17, 12, 1, 'Pretty Bad')
 ;

INSERT INTO UserToUser_Reviews (
	user_id_ratable, 
	user_id_consumer, 
	value,
	review
)
VALUES (19, 15, 1, 'Very tasty food, speedy delivery')
 ;


INSERT INTO _Order (
	tip,
    order_time,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (1, '2022-07-31 18:11:50', 0, "Im ordering from every restaurant haha", 2, 2, 1);

INSERT INTO _Order (
	tip,
    order_time,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (1, '2022-07-31 18:11:50', 0, "Im ordering from every restaurant haha", 2, 3, 1);

INSERT INTO _Order (
	tip,
    order_time,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (1, '2022-07-31 18:11:50', 0, "Im ordering from every restaurant haha", 2, 7, 1);
INSERT INTO _Order (
	tip,
    order_time,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (1, '2022-07-31 18:11:50', 0, "Im ordering from every restaurant haha", 2, 9, 1);

INSERT INTO _Order (
	tip,
    order_time,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (1, '2022-07-31 18:11:50', 0, "Im ordering from every restaurant haha", 2, 10, 1);

INSERT INTO _Order (
	tip,
    order_time,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (1, '2022-07-31 18:11:50', 0, "Im ordering from every restaurant haha", 2, 11, 1);
INSERT INTO _Order (
	tip,
    order_time,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (1, '2022-07-31 18:11:50', 0, "Im ordering from every restaurant haha", 2, 13, 1);
INSERT INTO _Order (
	tip,
    order_time,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (1, '2022-07-31 18:11:50', 0, "Im ordering from every restaurant haha", 2, 14, 1);
INSERT INTO _Order (
	tip,
    order_time,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (1, '2022-07-31 18:11:50', 0, "Im ordering from every restaurant haha", 2, 15, 1);
INSERT INTO _Order (
	tip,
    order_time,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (1, '2022-07-31 18:11:50', 0, "Im ordering from every restaurant haha", 2, 17, 1);
INSERT INTO _Order (
	tip,
    order_time,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (1, '2022-07-31 18:11:50', 0, "Im ordering from every restaurant haha", 2, 18, 1);
INSERT INTO _Order (
	tip,
    order_time,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (1, '2022-07-31 18:11:50', 0, "Im ordering from every restaurant haha", 2, 19, 1);
INSERT INTO _Order (
	tip,
    order_time,
	status, 
	special_instructions, 
	consumer_id, 
	restaurant_id, 
	speeder_id
)
VALUES (1, '2022-07-31 18:11:50', 0, "Im ordering from every restaurant haha", 2, 20, 1);