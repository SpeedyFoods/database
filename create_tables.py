import mysql.connector

db = mysql.connector.connect(
    host="database-1.crb52cpzkqln.us-west-1.rds.amazonaws.com",
    passwd="speedyfoods321",
    user="admin",
    database="testdatabase"
)

mycursor = db.cursor()

# create_person_table_query = "CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)"
# mycursor.execute(create_person_table_query)

mycursor.execute("show tables")

for x in mycursor:
    print(x)

db.close()