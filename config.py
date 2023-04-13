import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="testovaci_databaze"
)


weight_list = ["Under 40", "40-49", "50-59", "60-69", "70-79", "80-89", "90-99", "100-110", "over 110"]
seznam_cviku = ["SZU", "TEST", "JIN", "FTVS_A", "FTVS_J"]


sharing_option = ["YES - including face", "Limited - with anonymize face", "Only for research"]
gender = ["Man", "Woman", "Don't want to say"]
age_range = ["Under 18", "18-25", "26-33", "34-41", "42-49", "50-57", "58-65", "over 65"]

mycursor2 = mydb.cursor()
mycursor2.execute("SELECT Jmeno FROM prvni_tabulka")
myresult = mycursor2.fetchall()
lastnames = []
for row in myresult:
    for field in row:
        lastnames.append(field)

print(type(myresult))
seznam_subjektu = set(lastnames)

names_of_video_files = []


cam_1 = "rtsp://admin:kamera_fyzio_0" + str(1) + "@192.168.1.11" + str(1) + ":554/cam/realmonitor?channel=1&subtype=0"
cam_2 = "rtsp://admin:kamera_fyzio_0" + str(2) + "@192.168.1.12" + str(2) + ":554/cam/realmonitor?channel=1&subtype=0"
cam_3 = "rtsp://admin:kamera_fyzio_0" + str(3) + "@192.168.1.13" + str(3) + ":554/cam/realmonitor?channel=1&subtype=0"
cam_4 = "rtsp://admin:kamera_fyzio_0" + str(4) + "@192.168.1.14" + str(4) + ":554/cam/realmonitor?channel=1&subtype=0"

