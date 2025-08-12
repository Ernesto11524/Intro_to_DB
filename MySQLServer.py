import mysql.connector
from mysql.connector import Error

try:
    server = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Naakmp@30.'
    )

    cursor = server.cursor()
    cursor.execute("DROP DATABASE IF EXISTs alx_book_store")
    my_db = cursor.execute("CREATE DATABASE alx_book_store")
    server.commit
    if server.is_connected():
        print("Database 'alx_book_store' created successfully!")

    cursor.close()
    server.close()

except Error as e:
    print("Error while connecting to MySQL:", e)