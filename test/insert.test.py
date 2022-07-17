import sys
sys.path.append('..')
from db_client import db, cursor
from queries.insert_queries import insert_user_query

def insert_user_test():
    insert_tuple = ("tomi", "tomi@gmail.com", "7786966999", 0)
    cursor.execute(insert_user_query, insert_tuple)
    db.commit()
    print("user inserted successfully")

insert_user_test()