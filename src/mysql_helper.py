import mysql.connector

host_name = '35.189.35.6'
user = 'root'
password = 'comp3900'
database = 'waitlist_db'

def create_server_connection(host_name, user_name, user_password, database_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name, 
            user = user_name, 
            password = user_password, 
            database = database_name
        )
        print("connection created")
    except mysql.connector.Error as err:
        print(err)
    
    return connection

def insert_into_database(query, values, database):
    cursor = database.cursor()
    cursor.execute(query,values)
    database.commit()
