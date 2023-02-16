from PySide6 import QtCore, QtWidgets, QtGui

import config

import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="testovaci_databaze"
)











class ConfirmationWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # inicializace

        self.setWindowTitle("Confirmation Widow")
        self.info_text = QtWidgets.QLabel("Tool to add inform consent")
        self.edit_nickname = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton("OK")
        self.text_nickname = QtWidgets.QLabel("Add some funny nickname as ID")


        # Layout
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.info_text)
        self.layout.addWidget(self.text_nickname)
        self.layout.addWidget(self.edit_nickname)
        self.layout.addWidget(self.button)


        # Vlastnosti
        self.button.clicked.connect(self.save_info_to_database)
    def save_info_to_database(self):

        print(config.names_of_video_files)
        mycursor3 = mydb.cursor()
        # sql = "INSERT INTO prvni_tabulka (Jmeno,Vek, Prijmeni) VALUES (%s,%s, %s)"
        # val = (self.edit.text(), int(self.weight_comboBox.text()), self.edit2.text())
        listToStr = ' '.join([str(elem) for elem in config.names_of_video_files])
        sql = "INSERT INTO file_names_and_comments (file_name, comment) VALUES (%s, %s)"

        val = (listToStr, listToStr)
        mycursor3.execute(sql, val)
        mydb.commit()

        self.close()

        config.names_of_video_files.clear()