import sys
sys.path.append('..')
from db_client import db, cursor

def select_user_test():
    cursor.execute("select * from Users;")
    for table_name in cursor:
        print(table_name)

select_user_test()