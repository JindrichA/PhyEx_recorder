


import mysql.connector
from secrets_jindrich import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME




try:
    # Establish connection to the MySQL database
    mydb = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    # Create a new cursor
    mycursor = mydb.cursor()

    # Define your data
    figurant_id = 1  # Just an example; replace with your data
    exercise_type_id = 2  # Replace with your data
    datetime_value = "2023-09-12 14:00:00"  # Replace with your datetime format
    video_front = "video_front_path.mp4"  # Replace with your path or link
    video_side_video_mid_left = "video_side_mid_left_path.mp4"  # Replace with your path or link
    video_mid_right = "video_mid_right_path.mp4"  # Replace with your path or link

    # SQL Insertion query
    sql = (
        "INSERT INTO exercise "
        "(figurant_id, exercise_type_id, datatime, video_front, video_side_video_mid_left, video_mid_right) "
        "VALUES (%s, %s, %s, %s, %s, %s)"
    )
    val = (figurant_id, exercise_type_id, datetime_value, video_front, video_side_video_mid_left, video_mid_right)

    # Execute the query
    mycursor.execute(sql, val)

    # Commit the transaction
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")

finally:
    # Close the connection (in case it was established)
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection is closed")