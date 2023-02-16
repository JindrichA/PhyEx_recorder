import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import ffmpeg
import datetime
from datetime import datetime, timedelta
from datetime import timezone
import time
import cv2


import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="testovaci_databaze"
)
mycursor2 = mydb.cursor()
mycursor2.execute("SELECT Jmeno FROM prvni_tabulka")
myresult = mycursor2.fetchall()
lastnames = []
for row in myresult:
    for field in row:
        lastnames.append(field)



print(type(myresult))
seznam_subjektu = set(lastnames)


class AddSubjectWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # inicializace
        self.setWindowTitle("Subject details")
        self.edit_nickname = QtWidgets.QLineEdit()
        self.age_comboBox = QtWidgets.QComboBox()
        self.weight_comboBox = QtWidgets.QComboBox()
        self.button = QtWidgets.QPushButton("Add_subject")
        self.info_text = QtWidgets.QLabel("Tool to add inform consent")
        self.text_nickname = QtWidgets.QLabel("Add some funny nickname as ID")
        self.text_age = QtWidgets.QLabel("Add your age?")
        self.text_weight = QtWidgets.QLabel("Add your weight?")
        self.text_gender = QtWidgets.QLabel("What is your gender?")
        self.video_rights_text = QtWidgets.QLabel("Video rights, what can we do with the video?")

        self.multiplechoice = QtWidgets.QComboBox()
        self.checkbox_agree = QtWidgets.QCheckBox("Inform consent signed")
        self.gender_comboBox = QtWidgets.QComboBox()
        # Layout
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.info_text)
        self.layout.addWidget(self.text_nickname)
        self.layout.addWidget(self.edit_nickname)
        self.layout.addWidget(self.text_gender)
        self.layout.addWidget(self.gender_comboBox)
        self.layout.addWidget(self.text_age)
        self.layout.addWidget(self.age_comboBox)
        self.layout.addWidget(self.text_weight)
        self.layout.addWidget(self.weight_comboBox)
        self.layout.addWidget(self.video_rights_text)
        self.layout.addWidget(self.multiplechoice)



        self.layout.addWidget(self.checkbox_agree)
        self.layout.addWidget(self.button)


        # Vlastnosti
        self.button.clicked.connect(self.run)
        self.multiplechoice.addItems(["YES - including face", "Limited - with anonymize face", "Only for research"])
        self.gender_comboBox.addItems(["Man", "Woman", "Don't want to say"])
        self.age_comboBox.addItems(["Under 18", "18-25", "26-33", "34-41", "42-49", "50-57", "58-65", "over 65"])
        self.weight_comboBox.addItems(["Under 40", "40-49", "50-59", "60-69", "70-79", "80-89", "90-99", "100-110", "over 110"])
    def run(self):

        if self.edit_nickname.text() not in seznam_subjektu and self.checkbox_agree.isChecked():
            mycursor = mydb.cursor()
            #sql = "INSERT INTO prvni_tabulka (Jmeno,Vek, Prijmeni) VALUES (%s,%s, %s)"
            #val = (self.edit.text(), int(self.weight_comboBox.text()), self.edit2.text())
            sql = "INSERT INTO prvni_tabulka (Jmeno,Vek, Prijmeni) VALUES (%s,%s, %s)"
            val = (self.edit_nickname.text(), 32, self.age_comboBox.currentText())

            mycursor.execute(sql, val)
            mydb.commit()
            seznam_subjektu.add(self.edit_nickname.text())
            self.info_text.setText("Sucessfully saved to databse")
            self.info_text.setStyleSheet("color: green")
        else:
            self.info_text.setText("Was not saved to database!, Consent not provided or dublicite Nickname")
            self.info_text.setStyleSheet("color: red")


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Inicializace
        self.setWindowTitle("PhyEx Recorder 0.2 Jindrich 02/2023")
        self.button = QtWidgets.QPushButton("Start recording")
        self.button2 = QtWidgets.QPushButton("Stop")
        self.button3 = QtWidgets.QPushButton("Add new subject")
        self.button4 = QtWidgets.QPushButton("Vybrat subjekt")
        self.checkbox_button = QtWidgets.QCheckBox("Kamera 1")
        self.checkbox_button2 = QtWidgets.QCheckBox("Kamera 2")
        self.checkbox_button3 = QtWidgets.QCheckBox("Kamera 3")
        self.checkbox_button4 = QtWidgets.QCheckBox("Kamera 4")
        self.text = QtWidgets.QLabel("Vyberte si cvičení a kamery",
                                     alignment=QtCore.Qt.AlignCenter)
        self.listWidget2 = QtWidgets.QListWidget()
        self.listWidget = QtWidgets.QListWidget()

        self.layout = QtWidgets.QVBoxLayout(self)


        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
    #    self.layout.addWidget(self.button4)
        self.layout.addWidget(self.checkbox_button)
        self.layout.addWidget(self.checkbox_button2)
        self.layout.addWidget(self.checkbox_button3)
        self.layout.addWidget(self.checkbox_button4)
        self.layout.addWidget(self.listWidget)
        self.layout.addWidget(self.listWidget2)

        # Vlastnosti
        self.listWidget.addItems(["SZU", "TEST", "JIN"])
        self.button.clicked.connect(self.run)
        self.button2.clicked.connect(self.stop)
        self.button3.clicked.connect(self.show_new_window)
       # self.button4.clicked.connect(self.select_subject)
        self.listWidget2.addItems(seznam_subjektu)
        self.listWidget.itemClicked.connect(self.itemActivated_event)
        self.listWidget2.itemClicked.connect(self.itemActivated_event2)
        self.ID_of_the_participant = "0"
        self.path_to_save_videos = "C:/Users/adolfjin/Videos/"
        self.name_of_the_exercise = "Not_selected"


    @QtCore.Slot()
    def itemActivated_event(self, item):
        self.name_of_the_exercise = (item.text())

    @QtCore.Slot()
    def itemActivated_event2(self, item):
        self.ID_of_the_participant = (item.text())

    @QtCore.Slot()
    def actualizite_text(self):

        self.listWidget2.clear()
        self.listWidget2.addItems(seznam_subjektu)


    def show_new_window(self):
        self.w = AddSubjectWindow()
        self.w.show()
        self.w.resize(800, 400)
        self.w.button.clicked.connect(widget.actualizite_text)

    def select_subject(self):
        print("subject selected")

    @QtCore.Slot()
    def run(self):
        self.dt = datetime.now(timezone.utc)
        self.utc_time = self.dt.replace(tzinfo=timezone.utc)
        self.utc_timestamp = int(self.utc_time.timestamp())
        self.name_of_video = str(self.utc_timestamp)
        self.kam_number = 1

        # Tady přidat, možnost ověření, že ta kamera je připojená, aby to případně vyhodilo hlášku že to nejde


        if self.checkbox_button.isChecked():
            self. process_X = (
                ffmpeg
                .input(filename="rtsp://admin:kamera_fyzio_0"+str(1)+"@192.168.1.11"+str(1)+":554/cam/realmonitor?channel=1&subtype=0")
                .output(filename=self.path_to_save_videos+self.name_of_the_exercise+"_"+self.name_of_video+"_ID_"+self.ID_of_the_participant+"_cam_"+str(1)+".mp4", c="copy")
                .overwrite_output()
            )
            self.process1 = self.process_X.run_async(pipe_stdin=True)

        if self.checkbox_button2.isChecked():
            self. process_X2 = (
                ffmpeg
                .input(filename="rtsp://admin:kamera_fyzio_0"+str(2)+"@192.168.1.11"+str(2)+":554/cam/realmonitor?channel=1&subtype=0")
                .output(filename=self.path_to_save_videos+self.name_of_the_exercise+"_"+self.name_of_video+"_ID_"+self.ID_of_the_participant+"_cam_"+str(2)+".mp4", c="copy")
                .overwrite_output()
            )
            self.process2 = self.process_X2.run_async(pipe_stdin=True)

        if self.checkbox_button3.isChecked():
            self. process_X3 = (
                ffmpeg
                .input(filename="rtsp://admin:kamera_fyzio_0"+str(3)+"@192.168.1.11"+str(3)+":554/cam/realmonitor?channel=1&subtype=0")
                .output(filename=self.path_to_save_videos+self.name_of_the_exercise+"_"+self.name_of_video+"_ID_"+self.ID_of_the_participant+"_cam_"+str(3)+".mp4", c="copy")
                .overwrite_output()
            )
            self.process3 = self.process_X3.run_async(pipe_stdin=True)

        if self.checkbox_button4.isChecked():
            self. process_X4 = (
                ffmpeg
                .input(filename="rtsp://admin:kamera_fyzio_0"+str(4)+"@192.168.1.11"+str(4)+":554/cam/realmonitor?channel=1&subtype=0")
                .output(filename=self.path_to_save_videos+self.name_of_the_exercise+"_"+self.name_of_video+"_ID_"+self.ID_of_the_participant+"_cam_"+str(4)+".mp4", c="copy")
                .overwrite_output()
            )
            self.process4 = self.process_X4.run_async(pipe_stdin=True)


        self.text.setText("Video is recording: "+self.name_of_the_exercise)
        self.text.setStyleSheet("color: red")



    @QtCore.Slot()
    def stop(self):
        self.text.setText("Please wait...")
        self.total_fps = []
        if self.checkbox_button.isChecked():
            self.process1.communicate(str.encode("q"))
            #time.sleep(1)
            del self.process1
            video_1 = cv2.VideoCapture(self.path_to_save_videos+self.name_of_the_exercise+"_"+self.name_of_video+"_ID_"+self.ID_of_the_participant+"_cam_"+str(1)+".mp4")
            self.total_fps.append(int(video_1.get(cv2.CAP_PROP_FRAME_COUNT)))
            video_1.release()

        if self.checkbox_button2.isChecked():
            self.process2.communicate(str.encode("q"))
            #time.sleep(1)
            del self.process2
            video_2 = cv2.VideoCapture(self.path_to_save_videos+self.name_of_the_exercise+"_"+self.name_of_video+"_ID_"+self.ID_of_the_participant+"_cam_"+str(2)+".mp4")
            self.total_fps.append(int(video_2.get(cv2.CAP_PROP_FRAME_COUNT)))
            video_2.release()

        if self.checkbox_button3.isChecked():
            self.process3.communicate(str.encode("q"))
            #time.sleep(1)
            del self.process3
            video_3 = cv2.VideoCapture(self.path_to_save_videos+self.name_of_the_exercise+"_"+self.name_of_video+"_ID_"+self.ID_of_the_participant+"_cam_"+str(3)+".mp4")
            self.total_fps.append(int(video_3.get(cv2.CAP_PROP_FRAME_COUNT)))
            video_3.release()

        if self.checkbox_button4.isChecked():
            self.process4.communicate(str.encode("q"))
            #time.sleep(1)
            del self.process4
            video_4 = cv2.VideoCapture(self.path_to_save_videos+self.name_of_the_exercise+"_"+self.name_of_video+"_ID_"+self.ID_of_the_participant+"_cam_"+str(4)+".mp4")
            self.total_fps.append(int(video_4.get(cv2.CAP_PROP_FRAME_COUNT)))
            video_4.release()

        self.text.setText("OK videos had been recorded with total of {} frames.".format(self.total_fps))
        self.text.setStyleSheet("color: green")



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())