from PySide6 import QtCore, QtWidgets, QtGui
import config
import mysql.connector
from secrets_jindrich import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
import MainWindow
import re

mydb = mysql.connector.connect(
  host=DB_HOST,
  user=DB_USER,
  password=DB_PASSWORD,
  database=DB_NAME
)

class ConfirmationWindow(QtWidgets.QWidget):




    def __init__(self):
        super().__init__()
        # inicializace

        self.data_store = MainWindow.data_store
        self.setWindowTitle("Confirmation Widow")
        self.info_text = QtWidgets.QLabel("Tool to add inform consent")
        self.edit_comment = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton("OK")
        self.text_nickname = QtWidgets.QLabel("Add some funny nickname as ID")


        # Layout
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.info_text)
        self.layout.addWidget(self.text_nickname)
        self.layout.addWidget(self.edit_comment)
        self.layout.addWidget(self.button)


        # Vlastnosti
        self.button.clicked.connect(self.save_info_to_database)

    @QtCore.Slot()
    def itemActivated_event(self, item):
        self.name_of_the_exercise = (item.text())





    def save_info_to_database(self):
        def get_string_after_space(s):
            parts = s.split(" ", 1)  # Split the string at the first space

            if len(parts) > 1:
                return parts[1]  # Return the second part, which is the string after the space
            else:
                return None

        def get_number_before_space(s):
            pattern = r"(\d+)"
            match = re.match(pattern, s)

            if match:
                number = int(match.group(1))
                return number
            else:
                return None

        mycursor5 = mydb.cursor()
        string_nickname = get_string_after_space(self.data_store.shared_variable)
        query = "SELECT id FROM figurant WHERE nickname = %s"  # Use a parameter placeholder
        mycursor5.execute(query, (string_nickname,))  # Pass the variable as an argument
        myresult5 = mycursor5.fetchall()


        print(config.names_of_video_files)
        mycursor3 = mydb.cursor()
        # sql = "INSERT INTO prvni_tabulka (Jmeno,Vek, Prijmeni) VALUES (%s,%s, %s)"
        # val = (self.edit.text(), int(self.weight_comboBox.text()), self.edit2.text())
        list_to_str = ' '.join([str(elem) for elem in config.names_of_video_files])
        comment_from_edit = self.edit_comment.text()


        sql = "INSERT INTO exercise_comment (comment, exercise_ID) VALUES (%s, %s)"

        val = (comment_from_edit, int(myresult5[0][0]) )
        mycursor3.execute(sql, val)
        mydb.commit()

        self.close()

        config.names_of_video_files.clear()