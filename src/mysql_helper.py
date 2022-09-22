import mysql.connector

host = '35.189.35.6'
user = 'root'
password = 'comp3900'
database = 'waitlist_db'

#initialize connection to database
def create_server_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host, 
            user = user, 
            password = password, 
            database = database
        )
        print("connection created")
    except mysql.connector.Error as err:
        print(err)
    
    return connection

#inser into database base on the query and its data
def insert_into_database(query, values, database):
    cursor = database.cursor()
    cursor.execute(query,values)
    database.commit()

#clear connection to database
def end_db_session(database):
    database.close()

mydb = create_server_connection()
end_db_session(mydb)

