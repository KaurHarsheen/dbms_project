import cx_Oracle
import dotenv
import os

username = dotenv.get_key('.env', 'DB_USER')
password = dotenv.get_key('.env', 'DB_PASSWORD')
dsn = "172.16.64.222:1522/orclpdb"

team=[]

try:
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    
    print("Connection to Oracle database established successfully.")

    # Execute the query to retrieve data from EMP table
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM EMP")
    rows = cursor.fetchall()

    print(rows)

    cursor.close()
    connection.close()

except cx_Oracle.DatabaseError as e:
    print("Error connecting to Oracle database:", e)