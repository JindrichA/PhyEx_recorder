
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import ffmpeg
import datetime
from datetime import datetime, timedelta
from datetime import timezone
import time
import cv2

#ss

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
