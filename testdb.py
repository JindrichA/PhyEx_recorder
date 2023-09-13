import mysql.connector
from mysql.connector import Error
from secrets_jindrich import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
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



    test_mysql_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
