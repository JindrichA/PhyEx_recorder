from PySide6 import QtCore, QtWidgets, QtGui
import ffmpeg
import datetime
from datetime import datetime, timedelta
from datetime import timezone
import cv2
import numpy as np
import ConfirmationWindow
import config
import AddSubjectWindow
import config
import os
import platform
import subprocess
from data_store import DataStore
data_store = DataStore()


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # Inicializace
        self.data_store = data_store
        self.setWindowTitle("PhyEx Recorder 0.4 Jindrich 05/2023")
        self.button = QtWidgets.QPushButton("Start recording")
        self.button_stop = QtWidgets.QPushButton("Stop")
        self.button_add_subject = QtWidgets.QPushButton("Add new subject")
        self.button_update_database = QtWidgets.QPushButton("Update database")
        self.checkbox_button = QtWidgets.QCheckBox("Cam 1")
        self.checkbox_button2 = QtWidgets.QCheckBox("Cam 2")
        self.checkbox_button3 = QtWidgets.QCheckBox("Cam 3")
        self.checkbox_button4 = QtWidgets.QCheckBox("Cam 4")
        self.checkbox_button5 = QtWidgets.QCheckBox("Cam 5")
        self.checkbox_button6 = QtWidgets.QCheckBox("Cam 6")
        self.text = QtWidgets.QLabel("Select exercise and cameras",
                                     alignment=QtCore.Qt.AlignCenter)
        self.list_of_subjects = QtWidgets.QListWidget()
        self.listWidget = QtWidgets.QListWidget()

        self.layout = QtWidgets.QVBoxLayout(self)

        # Add the other widgets
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button_stop)

        # Create two horizontal layouts for the two columns
        left_column_layout = QtWidgets.QHBoxLayout()
        right_column_layout = QtWidgets.QHBoxLayout()

        # Add checkboxes to each column layout
        left_column_layout.addWidget(self.checkbox_button)
        left_column_layout.addWidget(self.checkbox_button2)
        left_column_layout.addWidget(self.checkbox_button3)
        right_column_layout.addWidget(self.checkbox_button4)
        right_column_layout.addWidget(self.checkbox_button5)
        right_column_layout.addWidget(self.checkbox_button6)

        # Add the two column layouts to the parent vertical layout
        self.layout.addLayout(left_column_layout)
        self.layout.addLayout(right_column_layout)

        # Continue adding the other widgets
        self.layout.addWidget(self.button_add_subject)
        self.layout.addWidget(self.listWidget)
        self.layout.addWidget(self.button_update_database)
        self.layout.addWidget(self.list_of_subjects)

        # Add a spacer to push the remaining widgets down
        self.layout.addStretch(1)

        # Vlastnosti
        self.listWidget.addItems(config.TYPE_OF_EXERCISE_LIST)
        self.button.clicked.connect(self.run)
        self.button_stop.clicked.connect(self.stop)
        self.button_add_subject.clicked.connect(self.show_new_window)
        self.button_update_database.clicked.connect(self.actualizite_text)
        self.list_of_subjects.addItems(sorted(config.seznam_subjektu))
        self.listWidget.itemClicked.connect(self.itemActivated_event)
        self.list_of_subjects.itemClicked.connect(self.itemActivated_event2)
        #self.list_of_subjects.itemClicked.connect(self.actualizite_text)
        self.ID_of_the_participant = "0"
        self.path_to_save_videos = config.PATH_TO_RECORDED_VIDEOS
        self.name_of_the_exercise = "Not_selected"

    def open_folder_in_explorer(self, folder_path):
        if not os.path.exists(folder_path):
            raise ValueError(f"Path '{folder_path}' does not exist.")

        if platform.system() == "Windows":
            subprocess.run(["explorer", os.path.abspath(folder_path)])
        elif platform.system() == "Darwin":
            subprocess.run(["open", os.path.abspath(folder_path)])
        elif platform.system() == "Linux":
            subprocess.run(["xdg-open", os.path.abspath(folder_path)])
        else:
            raise ValueError("Unsupported platform: " + platform.system())

    # Replace this with the path of the folder you want to open





    @QtCore.Slot()
    def itemActivated_event(self, item):
        self.name_of_the_exercise = (item.text())



    @QtCore.Slot()
    def itemActivated_event2(self, item):
        self.ID_of_the_participant = (item.text())

    @QtCore.Slot()
    def actualizite_text(self):

        self.list_of_subjects.clear()
        self.list_of_subjects.addItems(sorted(config.seznam_subjektu))


    def show_new_window(self):
        self.w = AddSubjectWindow.AddSubjectWindow()
        self.w.show()
        self.w.resize(800, 400)
     #   self.w.button.clicked.connect(widget.actualizite_text)
    def show_confirmation_window(self):
        self.cw = ConfirmationWindow.ConfirmationWindow()
        self.cw.show()
        self.cw.resize(800, 400)

    def testDevice(self, source):
        self.cap = cv2.VideoCapture(source)
        if self.cap is None or not self.cap.isOpened():
            print('Warning: unable to open video source: ', source)

    def select_subject(self):
        print("subject selected")

    @QtCore.Slot()
    def run(self):
        self.dt = datetime.now(timezone.utc)
        self.utc_time = self.dt.replace(tzinfo=timezone.utc)
        self.utc_timestamp = int(self.utc_time.timestamp())
        self.utc_timestamp = str(self.utc_timestamp)
        self.kam_number = 1
        self.data_store.shared_variable = self.list_of_subjects.currentItem().text()
        # Tady přidat, možnost ověření, že ta kamera je připojená, aby to případně vyhodilo hlášku že to nejde


        if self.checkbox_button.isChecked():
            self.process_X = (
                ffmpeg
                .input(filename=config.cam_1)
                .output(filename=self.path_to_save_videos+self.name_of_the_exercise+"_"+self.utc_timestamp+"_ID_"+self.ID_of_the_participant+"_cam_"+str(1)+".mp4", c="copy")
                .overwrite_output()
            )



            self.process1 = self.process_X.run_async(pipe_stdin=True)
        if self.checkbox_button2.isChecked():
            self. process_X2 = (
                ffmpeg
                .input(filename=config.cam_2)
                .output(filename=self.path_to_save_videos+self.name_of_the_exercise+"_"+self.utc_timestamp+"_ID_"+self.ID_of_the_participant+"_cam_"+str(2)+".mp4", c="copy")
                .overwrite_output()
            )

            self.process2 = self.process_X2.run_async(pipe_stdin=True)

        if self.checkbox_button3.isChecked():
            self. process_X3 = (
                ffmpeg
                .input(filename=config.cam_3)
                .output(filename=self.path_to_save_videos+self.name_of_the_exercise+"_"+self.utc_timestamp+"_ID_"+self.ID_of_the_participant+"_cam_"+str(3)+".mp4", c="copy")
                .overwrite_output()
            )

            self.process3 = self.process_X3.run_async(pipe_stdin=True)

        if self.checkbox_button4.isChecked():
            self. process_X4 = (
                ffmpeg
                .input(filename=config.cam_4)
                .output(filename=self.path_to_save_videos+self.name_of_the_exercise+"_"+self.utc_timestamp+"_ID_"+self.ID_of_the_participant+"_cam_"+str(4)+".mp4", c="copy")
                .overwrite_output()
            )
            self.process4 = self.process_X4.run_async(pipe_stdin=True)

        if self.checkbox_button5.isChecked():
            self. process_X5 = (
                ffmpeg
                .input(filename=config.cam_5)
                .output(filename=self.path_to_save_videos+self.name_of_the_exercise+"_"+self.utc_timestamp+"_ID_"+self.ID_of_the_participant+"_cam_"+str(5)+".mp4", c="copy")
                .overwrite_output()
            )
            self.process5 = self.process_X5.run_async(pipe_stdin=True)

        if self.checkbox_button6.isChecked():
            self. process_X6 = (
                ffmpeg
                .input(filename=config.cam_6)
                .output(filename=self.path_to_save_videos+self.name_of_the_exercise+"_"+self.utc_timestamp+"_ID_"+self.ID_of_the_participant+"_cam_"+str(6)+".mp4", c="copy")
                .overwrite_output()
            )
            self.process6 = self.process_X6.run_async(pipe_stdin=True)



        self.text.setText("Video is recording: "+self.name_of_the_exercise)
        self.text.setStyleSheet("color: red")



    @QtCore.Slot()
    def stop(self):
        self.text.setText("Please wait...")
        self.frame_count = []
        if self.checkbox_button.isChecked():
            self.process1.communicate(str.encode("q"))
            #time.sleep(1)
            del self.process1
            video_1 = cv2.VideoCapture(self.path_to_save_videos+self.name_of_the_exercise+"_"+self.utc_timestamp+"_ID_"+self.ID_of_the_participant+"_cam_"+str(1)+".mp4")
            self.frame_count.append(int(video_1.get(cv2.CAP_PROP_FRAME_COUNT)))
            config.names_of_video_files.append(self.name_of_the_exercise + "_" + self.utc_timestamp + "_ID_" + self.ID_of_the_participant + "_cam_" + str(1) + ".mp4")
            video_1.release()

        if self.checkbox_button2.isChecked():
            self.process2.communicate(str.encode("q"))
            #time.sleep(1)
            del self.process2
            video_2 = cv2.VideoCapture(self.path_to_save_videos+self.name_of_the_exercise+"_"+self.utc_timestamp+"_ID_"+self.ID_of_the_participant+"_cam_"+str(2)+".mp4")
            self.frame_count.append(int(video_2.get(cv2.CAP_PROP_FRAME_COUNT)))
            config.names_of_video_files.append(self.name_of_the_exercise + "_" + self.utc_timestamp + "_ID_" + self.ID_of_the_participant + "_cam_" + str(2) + ".mp4")
            video_2.release()

        if self.checkbox_button3.isChecked():
            self.process3.communicate(str.encode("q"))
            #time.sleep(1)
            del self.process3
            video_3 = cv2.VideoCapture(self.path_to_save_videos+self.name_of_the_exercise+"_"+self.utc_timestamp+"_ID_"+self.ID_of_the_participant+"_cam_"+str(3)+".mp4")
            self.frame_count.append(int(video_3.get(cv2.CAP_PROP_FRAME_COUNT)))
            config.names_of_video_files.append(self.name_of_the_exercise+"_"+self.utc_timestamp + "_ID_" + self.ID_of_the_participant + "_cam_" + str(3) + ".mp4")
            video_3.release()

        if self.checkbox_button4.isChecked():
            self.process4.communicate(str.encode("q"))
            #time.sleep(1)
            del self.process4
            video_4 = cv2.VideoCapture(self.path_to_save_videos+self.name_of_the_exercise+"_"+self.utc_timestamp+"_ID_"+self.ID_of_the_participant+"_cam_"+str(4)+".mp4")
            config.names_of_video_files.append(self.name_of_the_exercise+"_"+self.utc_timestamp + "_ID_" + self.ID_of_the_participant + "_cam_" + str(4) + ".mp4")
            self.frame_count.append(int(video_4.get(cv2.CAP_PROP_FRAME_COUNT)))
            video_4.release()

        if self.checkbox_button5.isChecked():
            self.process5.communicate(str.encode("q"))
            #time.sleep(1)
            del self.process5
            video_5 = cv2.VideoCapture(self.path_to_save_videos+self.name_of_the_exercise+"_"+self.utc_timestamp+"_ID_"+self.ID_of_the_participant+"_cam_"+str(5)+".mp4")
            config.names_of_video_files.append(self.name_of_the_exercise+"_"+self.utc_timestamp + "_ID_" + self.ID_of_the_participant + "_cam_" + str(5) + ".mp4")
            self.frame_count.append(int(video_5.get(cv2.CAP_PROP_FRAME_COUNT)))
            video_5.release()

        if self.checkbox_button6.isChecked():
            self.process6.communicate(str.encode("q"))
            #time.sleep(1)
            del self.process6
            video_6 = cv2.VideoCapture(self.path_to_save_videos+self.name_of_the_exercise+"_"+self.utc_timestamp+"_ID_"+self.ID_of_the_participant+"_cam_"+str(6)+".mp4")
            config.names_of_video_files.append(self.name_of_the_exercise+"_"+self.utc_timestamp + "_ID_" + self.ID_of_the_participant + "_cam_" + str(6) + ".mp4")
            self.frame_count.append(int(video_6.get(cv2.CAP_PROP_FRAME_COUNT)))
            video_6.release()

        self.text.setText("OK videos had been recorded with total of {} frames.".format(self.frame_count))
        self.text.setStyleSheet("color: green")
        self.show_confirmation_window()
        self.open_folder_in_explorer(config.PATH_TO_RECORDED_VIDEOS)
