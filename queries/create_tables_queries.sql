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
)

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
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE UserToUser_Reviews (
    user_id_ratable INTEGER, 
    user_id_consumer INTEGER NOT NULL, 
    rating_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    value  INTEGER NOT NULL,
    review TEXT,
    PRIMARY KEY (user_id_ratable, user_id_consumer, rating_time),
    FOREIGN KEY (User_id_consumer) REFERENCES User(user_id),
    CHECK (value >= 1 AND value <= 5)
);

CREATE TABLE Speeder (
    speeder_id INTEGER,
    transit INTEGER NOT NULL, 
    current_long FLOAT NOT NULL, 
    current_lat FLOAT NOT NULL,
    PRIMARY KEY (speeder_id),
    FOREIGN KEY (speeder_id) REFERENCES User(user_id),
    CHECK (transit >= 0 AND transit <= 2),
    CHECK (current_long >= -180 AND current_long <= 180), 
    CHECK (current_lat >= -90 AND current_lat <= 90)
);

CREATE TABLE Restaurant (
    restaurant_id INTEGER,
    restaurant_name CHAR(50) UNIQUE,
    PRIMARY KEY (restaurant_id),
    FOREIGN KEY (restaurant_name) References RestaurantParent(restaurant_name),
    FOREIGN KEY (restaurant_id) REFERENCES User(user_id)
);

CREATE TABLE Card_All (
    card_number_6 CHAR(6), 
    card_number_rest CHAR(10),
    expiration_date DATE NOT NULL, 
    zip CHAR(6) NOT NULL,
    user_id INTEGER NOT NULL, 
    PRIMARY KEY (card_number_6, card_number_rest),
    FOREIGN KEY (zip) REFERENCES Zip(zip),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (card_number_6) REFERENCES Card_BIN(card_number_6)
);

CREATE TABLE Item (
    item_name CHAR(20), 
    restaurant_id INTEGER,
    price FLOAT NOT NULL,
    PRIMARY KEY (item_name, restaurant_id),
    FOREIGN KEY (restaurant_id) REFERENCES Restaurant(restaurant_id)
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
    FOREIGN KEY (consumer_id) REFERENCES User(user_id),
    FOREIGN KEY (restaurant_id) REFERENCES Restaurant(restaurant_id),
    FOREIGN KEY (speeder_id) REFERENCES Speeder(speeder_id),
    CHECK (status <= 3 AND status >= 0)
);

CREATE TABLE OrderToItem (
    order_id INTEGER,
    restaurant_id INTEGER,
    item_name CHAR(20),
    PRIMARY KEY (order_id, restaurant_id, item_name),
    FOREIGN KEY (order_id) REFERENCES _Order(order_id),
    FOREIGN KEY (item_name, restaurant_id) REFERENCES Item(item_name, restaurant_id)
);
