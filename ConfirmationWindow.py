from PySide6 import QtCore, QtWidgets, QtGui

import config

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
        self.button.clicked.connect(self.run)
    def run(self):

        print("will be saved to database")
        self.close()