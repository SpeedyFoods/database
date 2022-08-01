import mysql.connector

local = True
if local:
    host = "localhost"
    user = "root"
else:
    host = "database-1.crb52cpzkqln.us-west-1.rds.amazonaws.com"
    user = "admin"

db = mysql.connector.connect(
    host=host,
    passwd="speedyfoods321",
    user=user,
    database="testdatabase"
)

cursor = db.cursor(buffered=True)