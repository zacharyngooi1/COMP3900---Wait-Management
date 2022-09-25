import mysql.connector
from mysql.connector import Error
import pandas as pd


def create_server_connection(host_name, user_name, user_password,database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database = database
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

pw = "Comp390012!"

mydb = create_server_connection("localhost", "root", pw, "wait_management")

mycursor = mydb.cursor()

def show_databases():
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
      print(x)


def create_restaurant(restaurant_name):

    mycursor.execute("CREATE TABLE %s (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))" % restaurant_name)

def show_tables():

    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)

print("databases are:")
show_databases()
print("tables are:")
show_tables()