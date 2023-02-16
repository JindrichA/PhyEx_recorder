import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import ffmpeg
import datetime
from datetime import datetime, timedelta
from datetime import timezone
import time
import cv2


import MainWindow



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow.MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())