import mysql.connector
from secrets_jindrich import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME



try:
    mydb = mysql.connector.connect(
      host=DB_HOST,
      user=DB_USER,
      password=DB_PASSWORD,
      database=DB_NAME
    )
    mycursor2 = mydb.cursor()
    mycursor2.execute("SELECT id, Nickname FROM figurant")
    myresult = mycursor2.fetchall()


except:
    print("Cannot connect to the database")
    myresult = ["No connection to the database"]

PATH_TO_RECORDED_VIDEOS = "C:/Users/adolfjin/videos_ip_cam/"



WEIGHT_LIST = ["Under 40", "40-49", "50-59", "60-69", "70-79", "80-89", "90-99", "100-110", "over 110"]
TYPE_OF_EXERCISE_LIST = ["1LBR", "TEST", "BRK4", "BRKZ", "FRLG", "GLUT", "HMST", "CHOP", "IPST", "LGST", "LTLG", "LTPL", "OLDL", "PLNK", "RFSN", "SKIS", "SMSQ", "SQUA" "YMWS", "YPST", "chessboard"]


SHARING_OPTION = ["YES - public with blur face", "Limited - Blur face for research only", "No share at all"]
FIGURANT_GENDER = ["Man", "Woman", "Don't want to say"]
FIGURANT_AGE = ["Under 18", "18-25", "26-33", "34-41", "42-49", "50-57", "58-65", "over 65"]
HOURS_SITTING_PER_DAY_LIST = ["Under 2 hours", "2-4 hours", "4-6 hours", "6-8 hours", "8-10 hours", "10-12 hours", "12-14 hours", "14-16 hours", "16-18 hours", "18-20 hours", "over 20 hours"]
ACTIVE_HOURS_PER_WEEK_LIST = ["Under 2 hours", "2-4 hours", "4-6 hours", "6-8 hours", "8-10 hours", "10-12 hours", "12-14 hours", "14-16 hours", "16-18 hours", "18-20 hours", "over 20 hours"]
INTENSIVE_SPORT_HOURS_PER_WEEK_LIST = ["Under 2 hours", "2-4 hours", "4-6 hours", "6-8 hours", "8-10 hours", "10-12 hours", "12-14 hours", "14-16 hours", "16-18 hours", "18-20 hours", "over 20 hours"]
STRETCHING_FREQUENCY_LIST = ["Never", "Once a week", "Twice a week", "Three times a week", "Four times a week", "Five times a week", "Six times a week", "Seven times a week"]



lastnames = []
ides = []

current_ID = 0
current_Nickname = "None"


for row in myresult:
    ides.append(row[0])
    lastnames.append(row[1])

str_list = [str(number) for number in ides]

print(type(myresult))
seznam_subjektu = merged_set = {" ".join(pair) for pair in zip(set(str_list), set(lastnames))}

names_of_video_files = []

# The default IP Cam for the camera befor setting up is http://192.168.1.108/


cams = [
    f"rtsp://admin:kamera_fyzio_0{i}@192.168.1.11{i}:554/cam/realmonitor?channel=1&subtype=0"
    for i in range(1, 7)
]

cam_1 = cams[0]
cam_2 = cams[1]
cam_3 = cams[2]
cam_4 = cams[3]
cam_5 = cams[4]
cam_6 = cams[5]


