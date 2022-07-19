from queries.create_tables_queries import *
from db_client import cursor, db

# The order in which the ddl statements are executed matters,
# since REFERENCES needs to reference a table that already has been created.

def delete_all_tables():
    cursor.execute("DROP DATABASE testdatabase;")
    cursor.execute("CREATE DATABASE testdatabase;")
    cursor.execute("use testdatabase;")

ddl = [
    create_card_bin_table_query,
    create_restaurant_parent_table_query,
    create_city_table_query,
    create_zip_table_query,
    create_user_table_query,
    create_user_address_table_query,
    create_user_to_user_table_query,
    create_speeder_table_query,
    create_restaurant_table_query,
    create_card_all_table_query,
    create_item_table_query,
    create_order_table_query,
    create_order_to_item_query,
]

if __name__ == "__main__":
# delete all tables before creating new ones
    delete_all_tables()

    # insert tables
    for statement in ddl: 
        cursor.execute(statement)
        # print(statement)

    db.commit()

    def show_tables():
        cursor.execute("SHOW tables;")
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)

    show_tables()
    db.close()
    print("Successfully created tables")
