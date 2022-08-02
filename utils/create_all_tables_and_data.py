"""
SQL Script
A single script that could be used to create all the tables and data in the database.
"""
from utils.insert_random_data_script import insert_random_data
from utils.create_tables import create_tables

if __name__ == "__main__":
    create_tables()
    insert_random_data()