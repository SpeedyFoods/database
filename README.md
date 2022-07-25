# Speedy Foods Database

## About Us:


## What We've Accomplisehd:

## How has our final schema differed from the schema we first Designed?


# Getting Started:

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


# 


# Endpoint Documentation

## /user_sign_up
payload example:
``` json
{
    "first_name": "tomiii",
    "last_name": "liu",
    "email": "tomi69@gmail.com",
    "phone": 77870777777,
    "type": 0,
    "zip": "V6R1Y9",
    "city": "vancouver",
    "building_number": 1111, 
    "unit_number": 0,
    "street_name": "Cambie st",
    "card_number": "1234561234567890",
    "expiration_date": 1234,
    "bank_name": "CIBC",
    "card_type": "debit",
    "payment_system": "visa"
}

```
## /place_order

## /register_restaurant

## /rate_restaurant

## /reset_database
- resets the database