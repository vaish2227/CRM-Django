import mysql.connector

database= mysql.connector.connect(
    host='localhost',
    user='root',
    password='root'
)

cursorObject=database.cursor()

cursorObject.execute("CREATE DATABASE djangoDB")
print("All Done!")