# Speedy Foods Database

## About Us:


## What We've Accomplisehd:

## How has our final schema differed from the schema we first Designed?


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