import mysql.connector

db = mysql.connector.connect(
    host="database-1.crb52cpzkqln.us-west-1.rds.amazonaws.com",
    passwd="speedyfoods321",
    user="admin",
    database="testdatabase"
)

mycursor = db.cursor()

# The order in which the ddl statements are executed matters,
# since REFERENCES needs to reference a table that already has been created.
ddl = [
    # (1) referenced by Card_All
    '''
    CREATE TABLE Card_BIN (
        card_number_6 CHAR(6),
        bank_name CHAR(50) NOT NULL,
        card_type CHAR(20) NOT NULL,
        payment_system CHAR(30) NOT NULL,
        PRIMARY KEY (card_number_6)
    );
    ''',

    # (2) referenced by Restaurant
    '''
    CREATE TABLE RestaurantParent (
        PRIMARY KEY restaurant_name char(50) NOT NULL,
        cuisine CHAR(20)
    )
    ''',

    # (3) referenced by Zip
    '''
    CREATE TABLE City (
        city_name CHAR(25) PRIMARY KEY,
        province_name CHAR(25)
    );
    ''',

    # (4) referenced by User_Address, Card_All
    '''CREATE TABLE Zip (
        zip CHAR(6),
        city_name CHAR(30) NOT NULL,
        PRIMARY KEY (zip),
        FOREIGN KEY (city_name) REFERENCES City(city_name)
    );
    ''',

    # (5) referenced by User_Address, UserToUser_Reviews, Speeder, Restaurant, Card_All
    ''' 
    CREATE TABLE User (
        user_id int,
        name CHAR(20) NOT NULL,
        email CHAR(30) NOT NULL,
        phone CHAR(20) NOT NULL,
        type int NOT NULL,
        PRIMARY KEY (user_id),
        CHECK (type <= 2 AND type >= 0)
    );
    ''',

    # (6)
    '''
    CREATE TABLE User_Address (
        address_id integer,
        user_id integer, 
        zip CHAR(6), 
        building_number integer, 
        unit_number integer, 
        street_name CHAR(50),
        PRIMARY KEY (address_id),
        FOREIGN KEY (zip) REFERENCES Zip(zip),
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    ''',

    # (7)
    '''
    CREATE TABLE UserToUser_Reviews (
        user_id_ratable INTEGER, 
        user_id_consumer INTEGER NOT NULL, 
        rating_time TIMESTAMP,
        value UNSIGNED INTEGER NOT NULL,
        review CHAR(256),
        PRIMARY KEY (user_id_ratable, user_id_consumer, rating_time),
        FOREIGN KEY (User_id_consumer) REFERENCES User(user_id),
        CHECK (value >= 1 AND value <= 5)
    );
    ''',

    # (8)
    '''
    CREATE TABLE Speeder (
        speeder_id INTEGER,
        transit INTEGER NOT NULL, 
        current_long FLOAT NOT NULL, 
        current_lat FLOAT NOT NULL,
        PRIMARY KEY (speeder_id),
        FOREIGN KEY (speeder_id) REFERENCES User(user_id),
        CHECK (current_long >= -180 AND current_long <= 180), 
        CHECK (current_lat >= -90 AND current_lat <= 90)
    );
    ''',

    # (9) referenced by Item, Order
    '''
    CREATE TABLE Restaurant (
        FOREIGN KEY restaurant_name References RestaurantParent(restaurant_name),
        FOREIGN KEY restaurant_id REFERENCES User(user_id),
	    PRIMARY KEY (restaurant_id)
    );
    ''',

    # (10)
    '''
    CREATE TABLE Card_All (
        card_number_6 char(6), 
        card_number_rest char(10),
        expiration_date DATE NOT NULL, 
        zip char(6) NOT NULL
        user_id integer NOT NULL, 
        PRIMARY KEY (card_number_6, card_number_rest),
        FOREIGN KEY zip REFERENCES Zip(zip),
        FOREIGN KEY (user_id) REFERENCES Users(user_id),
        FOREIGN KEY (card_number_6) REFERENCES Card_BIN(card_number_6)
    );
    ''',

    # (11) referenced by OrderToItem
    '''
    CREATE TABLE Item (
        item_name char(20), 
        restaurant_id integer,
        price float NOT NULL,
        PRIMARY KEY (item_name, restaurant_id),
        FOREIGN KEY (restaurant_id) REFERENCES Restaurant(restaurant_id)
    );
    ''',

    # (12) referenced by OrderToItem
    '''
    CREATE TABLE Order (
        order_id integer,
        tip float NOT NULL,
        status integer NOT NULL, 
        order_time timestamp NOT NULL, 
        special_instructions char(250), 
        consumer_id integer, 
        restaurant_id integer, 
        speeder_id integer,
        PRIMARY KEY (order_id),
        FOREIGN KEY (consumer_id) REFERENCES User(user_id),
        FOREIGN KEY (restaurant_id) REFERENCES Restaurant(restaurant_id),
        FOREIGN KEY (speeder_id) REFERENCES Speeder(speeder_id),
        CHECK (status <= 3 AND status >= 0)
    );
    ''',

    # (13)
    '''
    CREATE TABLE OrderToItem (
        order_id integer,
        restaurant_id integer,
        item_name char(20),
        PRIMARY KEY (order_id, restaurant_id, item_name),
        FOREIGN KEY (order_id) REFERENCES Order(order_id),
        FOREIGN KEY (item_name, restaurant_id) REFERENCES Item(item_name, restaurant_id)
    );
    '''
]

for statement in ddl: mycursor.execute(statement)

db.close()
