from db_client import cursor, db
from datetime import date, datetime
from random import randint, randrange
from queries.insert_queries import *
from insert_tables import insert_sample_rows
from create_tables import create_tables

from utils import delete_all_rows_from_database, list_of_tables


def select_sample_rows():  # Do I need to make a def similar to the one in select.test.py?
    cursor.execute("SELECT restaurant_name FROM RestaurantParent WHERE cuisine = 'Fast Food'")
    record = cursor.fetchall()  # cuisine was changed from Sushi to Fast Food, to match sample insertion

    for row in record:
        print("Name = ", row[0])  # Query selects restaurant names for which the cuisine is "Fast Food"

    cursor.execute("SELECT consumer_id FROM _Order")  # Projection query to find consumer_id for orders
    record = cursor.fetchall()

    for row in record:
        print("ID = ", row[0])

    cursor.execute("SELECT restaurant_name, Item.restaurant_id, item_name, price FROM Restaurant, Item WHERE "
                   "Restaurant.restaurant_id = Item.restaurant_id")  # Join query, gives restaurant and item info
    # removed restaurant_id from the SELECT, as it gave an error stating it as "ambiguous"
    record = cursor.fetchall()

    for row in record:
        print("Restaurant Name = ", row[0])
        print("Restaurant ID = ", row[1])
        print("Item Name = ", row[2])
        print("Price = ", row[3])  # Nice

    cursor.execute("SELECT COUNT(*) FROM RestaurantParent")  # Aggregate query, counts the number of restaurant brands
    record = cursor.fetchall()

    for row in record:
        print("Number of restaurant choices = ", row[0])

    cursor.execute("SELECT restaurant_id, MIN(price) FROM Item WHERE restaurant_id IN (SELECT restaurant_id FROM "
                   "Restaurant GROUP BY restaurant_name)")  # Nested aggregation with group-by, could someone check if this is appropriate?
    record = cursor.fetchall()

    for row in record:
        print("Restaurant ID = ", row[0])
        print("Minimum item price = ", row[1])

    # unable to code the "Division query part": An example of what could be done is all customers that have placed
    # an order at every restaurant, or something similar

    # cursor.execute("SELECT * FROM Order o WHERE NOT EXISTS ((SELECT r.restaurant_id FROM Restaurant r) EXCEPT (SELECT or.restaurant_id FROM Order ord WHERE ord.consumer_id = o.consumer_id))")
    # record = cursor.fetchall()
    #
    # for row in record:
    #     print("Print statements...")


if __name__ == "__main__":
    create_tables()
    insert_sample_rows()
    select_sample_rows()
