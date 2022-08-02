# Submission Checklist:
- [ ] make repository public
- [ ] paste git hash here **9a48869719fb95c7d2a1c5f815cd18a58a7841f4**
- [ ] submit link to canvas and verify that it is accessible publicly 

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


# Screenshots:



# Create all tables and insert all Data from an SQL Script

Copy the contents of `generate_all_tables_and_rows.sql` into MySQLWorkbench, then run the script.


# Setting Up DataBase:
First, you must have a MySQL database running. Edit the `db_client.py` with your
database credentials. 


# Running our Application Server (Flask) through the command line:
1. Install Python Dependencies:
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
$ flask run
```

# File Descriptions:

### `/app.py`
`/app.py` contains our Flask web framework that routes endpoints to the correct functions. It also serves web pages to the user.

### `/handlers.py`
`/handlers.py` contains the functions that handle the API endpoints.  All the logic for data insertions exist here.

###`/db_client.py`
`/db_client.py` is where the Flask framework initializes the `cursor` object that is used to manipulate the database. You would provide database credentials here, allowing Flask to connect to the database.

### `/queries/*`
this folder contains queries table creation and insertion queries. Selection queries are handled in `handlers.py`

### `/templates/*`
this folder contains Jinja templates. The templates turn into HTML and CSS, creating the user interface.
