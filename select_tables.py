from db_client import cursor, db
from datetime import date, datetime
from random import randint, randrange
from queries.insert_queries import *
from insert_tables import insert_sample_rows
from create_tables import create_tables

from utils import delete_all_rows_from_database, list_of_tables

def select_sample_rows():
    cursor.execute("SELECT restaurant_name FROM RestaurantParent WHERE cuisine = 'Fast Food'")
    record = cursor.fetchall()

    for row in record:
        print("Name = ", row[0])

    cursor.execute("SELECT consumer_id FROM _Order")
    record1 = cursor.fetchall()

    for row in record1:
        print("ID = ", row[0])


if __name__ == "__main__":
    create_tables()
    insert_sample_rows()
    select_sample_rows()