# Speedy Foods Database

## About Us:
Please read `/milestone_4_.pdf` for screenshots and summary.

# What We've Accomplisehd:
In milestone 4, we have built a complete application that has food delivery functionalities.
### Technology: 
Our team built a full stack application with html, python’s Flask API framework and mysql database.

### Usage:
#### Users can:
- register accounts by entering their email, address and credit card information
- Place orders from a restaurant
- Rate restaurants

#### Restaurant owners can
- register their companies with our app
- Add dishes to their restaurants

#### View:
- The app allows you to view all users in database
- Search for item from a restaurant
- Data validation on client and server side



# How has our final schema differed from the schema we first Designed?
Throughout our planning and development process, we have mostly used the schema that we turned in except for minor changes. 
Some changes that we’ve made:
- Separated Zip from Address into its own table since it can be a repeated value
- Separated city_name from Address into its own table since it can be a repeated value
- Added the auto keyword to timestamp and primary keys. This allows MySQL to handle indexing and creating time more efficiently than inserting these values - programmatically.
- Removed functional dependencies from credit card number Bank Identification Number (BIN). BIN is the first 6 values of every credit card number and this value contains information about the credit cards bank provider, credit card type (visa, mastercard), and whether or not it is debit or credit. Since this value can be shared by multiple different credit cards, we have separated Card_BIN6 into its own table from card_all.
- Previously, restaurants were a simple entity but we have changed it so that it must be owned/managed by a manager. For every restaurant in Restaurant table, it now has a foreign key that points to a manager in the User table. This value is provided in the restaurant sign up form.
- At first, we wanted to create tables to contain items (dishes with price) specifically for a restaurant (restaurant menu for users to order from), but we have improved it by creating  a single Item table to contain all Items from all restaurants. Each item in Item table has a foreign key that points to a restaurant. 

- Restaurant Items/Menu can be retrieved by simply writing a join query to find which restaurant the item belongs to. 

Overall we kept the original schema form. Our improvements led to creating even tables, which made the coding implementation harder because we have to write more - checks and insert data to more tables.


# Create all tables and insert all Data from SQL Script

copy the script inside `generate_all_tables_and_rows.sql` and run it.


# Setting Up DataBase:
First, you must have a sql database running. Create a database named `testdatabase` then edit the `db_client.py` with your
database credentials. 

run: 
``` bash
pip3 install -r requirements.txt
```

then create the tables and insert rows by running:
``` bash
pip3 create_all_tables_and_data.py
```


# Running our Application Server:
1. Install Python Dependency Packages:
mac:
``` bash
pip3 install -r requirements.txt
```


windows:
``` bash
pip install -r requirements.txt
```

2. Run the Server!
``` bash
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run
```

# File Descriptions:

### `/app.py`
`/app.py` contains our Flask web framework that routes endpoints to the correct functions. It also serves web pages to the user.

### `/handlers.py`
`/handlers.py` contains the functions that handle the API endpoints.  All the logic for data insertions exist here.

### `/insert_random_data_script.py`
This file automatically 

### `/queries/*`
this folder contains queries table creation and insertion queries. Selection queries are handled in `handlers.py`

# Endpoint Documentation

### /user_sign_up

### /place_order

### /insert_item
### /register_restaurant

### /rate_restaurant

### /reset_database
