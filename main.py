import sys
from PySide6 import QtCore, QtWidgets, QtGui

import MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow.MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())