import mysql.connector

connection = mysql.connector.connect(
    host="localhost",  # Yoki 127.0.0.1
    port=3306,
    user="root",
    password="12345"
)

print("MySQL bazaga muvaffaqiyatli ulandi!")
