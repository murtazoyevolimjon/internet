import json
import mysql.connector
import socket



connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password=""
)

cursor = connection.cursor()



def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS Internet")
    cursor.execute("USE Internet")
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS domain (
            id INT AUTO_INCREMENT PRIMARY KEY,
            domain VARCHAR(150),
            ip VARCHAR(150)
        )"""
    )



def insert_data(domain, ip):
    cursor.execute(
        "INSERT INTO domain (domain, ip) VALUES (%s, %s)",
        (domain, ip),
    )
    connection.commit()



def main():
    create_database()

    
    try:
        with open("domains.txt", "r") as file:
            domains = file.read().splitlines()
    except FileNotFoundError:
        print("domains.txt fayli topilmadi!")
        return

    
    for domain in domains:
        try:
            ip = socket.gethostbyname(domain)
            insert_data(domain, ip)
            print(f"{domain} -> {ip} bazaga yozildi!")
        except socket.gaierror:
            print(f" {domain} uchun IP topilmadi.")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
