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
    except mysql.connector.error as err:
        print(f"error creating connection ---------'{err}'")
    
    return connection

def insert_user_to_users_Table(query, value,db):
    cursor = db.cursor()
    cursor.execute(query,value)
    db.commit()

db = create_server_connection(host_name, user, password, database)
mycursor= db.cursor()

mycursor.execute("DROP TABLE IF EXISTS users")
mycursor.execute("CREATE TABLE users (user_id int NOT NULL AUTO_INCREMENT, name VARCHAR(15) NOT NULL, email VARCHAR(125) NOT NULL, password VARCHAR(64) NOT NULL, admin binary,PRIMARY KEY(user_id) )")

query = ("INSERT INTO users (name, email, password, admin)"
              "values (%s, %s, %s, %s)")

query1 = ("INSERT INTO users (name, email, password)"
              "values (%s, %s, %s)")

val = ("unsw", "unsw@unsw.com", "unsw", True)
val1 = ("unsw", "unsw@unsw.com", "unsw")

insert_user_to_users_Table(query,val,db)
insert_user_to_users_Table(query1,val1,db)

mycursor.execute("set global max_allowed_packet=67108864")

mycursor.close()
db.close()