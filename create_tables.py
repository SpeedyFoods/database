import mysql.connector

from db_client import cursor, db
# create_person_table_query = "CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)"
# mycursor.execute(create_person_table_query)

cursor.execute("show tables")

for x in cursor:
    print(x)

db.close()