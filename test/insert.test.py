import sys
sys.path.append('..')
from random import randint, randrange

from db_client import db, cursor
from queries.insert_queries import insert_user_query
from fake_values import fake_emails, fake_names

def get_random_phone_number():
    # returns a random 10 digit phone number
    return randint(1000000000,9999999999)

def get_random_user_type():
    return randint(0,3)

def delete_all_rows_from(table_name):
    cursor.execute(f"DELETE FROM {table_name};")

#
def insert_user_test():
    # insert_tuple = ("tomi", "tomi@gmail.com", "7786966999", 0)

    for i in range(10):
        insert_tuple = (fake_names[i], fake_emails[i], str(get_random_phone_number()), get_random_user_type())
        cursor.execute(insert_user_query, insert_tuple)
        db.commit()
    print("user inserted successfully")

def insert_card_bin():
    """
    CREATE TABLE Card_BIN (
    card_number_6 char(6),
    bank_name char(50) NOT NULL,
    card_type char(20) NOT NULL,
    payment_system char(30) NOT NULL,
    PRIMARY KEY (card_number_6)
    );
    """
    

# insert_user_test()
