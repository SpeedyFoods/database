import mysql.connector

db = mysql.connector.connect(
    host="database-1.crb52cpzkqln.us-west-1.rds.amazonaws.com",
    passwd="speedyfoods321",
    user="admin",
    database="testdatabase"
)

cursor = db.cursor()