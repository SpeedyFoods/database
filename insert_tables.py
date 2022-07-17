from db_client import db, cursor
import datetime

mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                        VALUES (%s, %s, %s, %s) """

current_Date = datetime.now()
# convert date in the format you want
formatted_date = current_Date.strftime('%Y-%m-%d %H:%M:%S')
insert_tuple = (7, 'Acer Predator Triton', 2435, current_Date)

result = cursor.execute(mySql_insert_query, insert_tuple)
