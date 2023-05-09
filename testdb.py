import mysql.connector
from mysql.connector import Error

def test_mysql_connection(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Connected to MySQL Database")
            connection.close()

    except Error as e:
        print("Error while connecting to MySQL Database:", e)

if __name__ == "__main__":
    # Replace these with your own database credentials
    host = "your_host"
    user = "your_username"
    password = "your_password"
    database = "your_database"

    test_mysql_connection('10.8.0.1', 'PhyexRecorder', 'asdahhksa566%EWr', 'phyex')
