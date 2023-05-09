

from PySide6 import QtCore, QtWidgets, QtGui
import time
import config
import mysql.connector
from secrets_jindrich import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME




mydb = mysql.connector.connect(
  host=DB_HOST,
  user=DB_USER,
  password=DB_PASSWORD,
  database=DB_NAME
)
#ss

class AddSubjectWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # inicializace
        self.setWindowTitle("Subject details")
        self.edit_nickname = QtWidgets.QLineEdit()
        self.age_comboBox = QtWidgets.QComboBox()
        self.weight_comboBox = QtWidgets.QComboBox()
        self.edit_occupation = QtWidgets.QLineEdit()
        self.sitting_per_day_comboBox = QtWidgets.QComboBox()
        self.active_hours_per_week_comboBox = QtWidgets.QComboBox()
        self.sport_hours_per_week_comboBox = QtWidgets.QComboBox()
        self.stretching_frequency_comboBox = QtWidgets.QComboBox()
        self.button = QtWidgets.QPushButton("Add_subject")
        self.info_text = QtWidgets.QLabel("Tool to add inform consent")
        self.text_nickname = QtWidgets.QLabel("Add some funny nickname as ID for example: 'Pepa'")
        self.text_occupation = QtWidgets.QLabel("What is your occupation? (student, worker, retired, ...)")
        self.text_sitting_per_day = QtWidgets.QLabel("How many hours do you sit per day?")
        self.text_strethig_frequency = QtWidgets.QLabel("How often do you stretch?")
        self.text_active_hours_per_week = QtWidgets.QLabel("How many hours per week do you spend by moderate activity, etc. walking, gardening, ...?")
        self.text_sport_hours_per_week = QtWidgets.QLabel("How many hours per week do you spend by intensive sport activity, etc. running, cycling, ...?")

        self.text_age = QtWidgets.QLabel("Add your age?")
        self.text_weight = QtWidgets.QLabel("Add your weight? [kg]")
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
        self.layout.addWidget(self.text_occupation)
        self.layout.addWidget(self.edit_occupation)
        self.layout.addWidget(self.text_gender)
        self.layout.addWidget(self.gender_comboBox)
        self.layout.addWidget(self.text_age)
        self.layout.addWidget(self.age_comboBox)
        self.layout.addWidget(self.text_weight)
        self.layout.addWidget(self.weight_comboBox)
        self.layout.addWidget(self.text_sitting_per_day)
        self.layout.addWidget(self.sitting_per_day_comboBox)
        self.layout.addWidget(self.text_active_hours_per_week)
        self.layout.addWidget(self.active_hours_per_week_comboBox)
        self.layout.addWidget(self.text_sport_hours_per_week)
        self.layout.addWidget(self.sport_hours_per_week_comboBox)
        self.layout.addWidget(self.text_strethig_frequency)
        self.layout.addWidget(self.stretching_frequency_comboBox)
        self.layout.addWidget(self.video_rights_text)
        self.layout.addWidget(self.multiplechoice)



        self.layout.addWidget(self.checkbox_agree)
        self.layout.addWidget(self.button)


        # Vlastnosti
        self.button.clicked.connect(self.run)
        self.multiplechoice.addItems(config.SHARING_OPTION)
        self.gender_comboBox.addItems(config.FIGURANT_GENDER)
        self.age_comboBox.addItems(config.FIGURANT_AGE)
        self.weight_comboBox.addItems(config.WEIGHT_LIST)
        self.sitting_per_day_comboBox.addItems(config.HOURS_SITTING_PER_DAY_LIST)
        self.active_hours_per_week_comboBox.addItems(config.ACTIVE_HOURS_PER_WEEK_LIST)
        self.sport_hours_per_week_comboBox.addItems(config.INTENSIVE_SPORT_HOURS_PER_WEEK_LIST)
        self.stretching_frequency_comboBox.addItems(config.STRETCHING_FREQUENCY_LIST)

    def run(self):

        if self.edit_nickname.text() not in config.seznam_subjektu and self.checkbox_agree.isChecked():
            mycursor = mydb.cursor()
            #sql = "INSERT INTO prvni_tabulka (Jmeno,Vek, Prijmeni) VALUES (%s,%s, %s)"
            #val = (self.edit.text(), int(self.weight_comboBox.text()), self.edit2.text())
            sql = "INSERT INTO figurant (firstname, surname, birth_year, gender, occupation, sitting_time_per_day, active_hours_per_week, stretching_frequency, weight, height) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            sql = "INSERT INTO figurant (gender, occupation, sitting_time_per_day, active_hours_per_week, stretching_frequency, weight, height, nickname, age, sport_hours_per_week) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            # val = (self.edit_nickname.text(), 32, self.age_comboBox.currentText())
            #val = ("John", self.edit_nickname.text(), self.age_comboBox.currentText(), "Male", "Developer", "6 hours", "30 hours", "Twice a day", 70, 170)
            #val = ("John", self.edit_nickname.text(), 1990, "Male", "Developer", "6 hours", "30 hours", "Twice a day", 70, 170)
            age = 20
            sport_hours_per_week = 10

            val = (self.gender_comboBox.currentText(), self.edit_occupation.text(), self.sitting_per_day_comboBox.currentText(),
                   self.active_hours_per_week_comboBox.currentText(), self.stretching_frequency_comboBox.currentText(), self.weight_comboBox.currentText(),
                   170, self.edit_nickname.text(), self.age_comboBox.currentText(), self.sport_hours_per_week_comboBox.currentText())


            mycursor.execute(sql, val)
            mydb.commit()
            config.seznam_subjektu.add(self.edit_nickname.text())
            self.info_text.setText("Sucessfully saved to databse")
            self.info_text.setStyleSheet("color: green")
            self.close()
        else:
            self.info_text.setText("Was not saved to database!, Consent not provided or dublicite Nickname")
            self.info_text.setStyleSheet("color: red")
