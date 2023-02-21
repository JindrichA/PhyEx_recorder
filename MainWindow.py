from PySide6 import QtCore, QtWidgets, QtGui
import ffmpeg
import datetime
from datetime import datetime, timedelta
from datetime import timezone

import cv2

import ConfirmationWindow
import config
import AddSubjectWindow




class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Inicializace
        self.setWindowTitle("PhyEx Recorder 0.2 Jindrich 02/2023")
        self.button = QtWidgets.QPushButton("Start recording")
        self.button_stop = QtWidgets.QPushButton("Stop")
        self.button_add_subject = QtWidgets.QPushButton("Add new subject")
        self.button_update_database = QtWidgets.QPushButton("Update database")
        self.checkbox_button = QtWidgets.QCheckBox("Camera 1")
        self.checkbox_button2 = QtWidgets.QCheckBox("Kamera 2")
        self.checkbox_button3 = QtWidgets.QCheckBox("Kamera 3")
        self.checkbox_button4 = QtWidgets.QCheckBox("Kamera 4")
        self.text = QtWidgets.QLabel("Vyberte si cvičení a kamery",
                                     alignment=QtCore.Qt.AlignCenter)
        self.list_of_subjects = QtWidgets.QListWidget()
        self.listWidget = QtWidgets.QListWidget()

        self.layout = QtWidgets.QVBoxLayout(self)


        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button_stop)
        self.layout.addWidget(self.button_add_subject)
        
        self.layout.addWidget(self.checkbox_button)
        self.layout.addWidget(self.checkbox_button2)
        self.layout.addWidget(self.checkbox_button3)
        self.layout.addWidget(self.checkbox_button4)
        self.layout.addWidget(self.listWidget)
        self.layout.addWidget(self.button_update_database)
        self.layout.addWidget(self.list_of_subjects)

        # Vlastnosti
        self.listWidget.addItems(["SZU", "TEST", "JIN"])
        self.button.clicked.connect(self.run)
        self.button_stop.clicked.connect(self.stop)
        self.button_add_subject.clicked.connect(self.show_new_window)
        self.button_update_database.clicked.connect(self.actualizite_text)
        self.list_of_subjects.addItems(config.seznam_subjektu)
        self.listWidget.itemClicked.connect(self.itemActivated_event)
        self.list_of_subjects.itemClicked.connect(self.itemActivated_event2)
        #self.list_of_subjects.itemClicked.connect(self.actualizite_text)
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

        self.list_of_subjects.clear()
        self.list_of_subjects.addItems(config.seznam_subjektu)


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
        self.name_of_video = str(self.utc_timestamp)
        self.kam_number = 1

        # Tady přidat, možnost ověření, že ta kamera je připojená, aby to případně vyhodilo hlášku že to nejde


        if self.checkbox_button.isChecked():
            cam1_filname = "rtsp://admin:kamera_fyzio_0" + str(2) + "@192.168.1.11" + str(1) + ":554/cam/realmonitor?channel=1&subtype=0"
            self.process_X = (
                ffmpeg
                .input(filename=cam1_filname)
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

            cam3_filname = "rtsp://admin:kamera_fyzio_0" + str(3) + "@192.168.1.11" + str(3) + ":554/cam/realmonitor?channel=1&subtype=0"
            #self.testDevice(cam3_filname)
            self. process_X3 = (
                ffmpeg
                .input(filename=cam3_filname)
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
            config.names_of_video_files.append( self.name_of_video + "_ID_" + self.ID_of_the_participant + "_cam_" + str(3) + ".mp4")
            video_3.release()

        if self.checkbox_button4.isChecked():
            self.process4.communicate(str.encode("q"))
            #time.sleep(1)
            del self.process4
            video_4 = cv2.VideoCapture(self.path_to_save_videos+self.name_of_the_exercise+"_"+self.name_of_video+"_ID_"+self.ID_of_the_participant+"_cam_"+str(4)+".mp4")
            config.names_of_video_files.append(self.name_of_video + "_ID_" + self.ID_of_the_participant + "_cam_" + str(4) + ".mp4")
            self.total_fps.append(int(video_4.get(cv2.CAP_PROP_FRAME_COUNT)))
            video_4.release()

        self.text.setText("OK videos had been recorded with total of {} frames.".format(self.total_fps))
        self.text.setStyleSheet("color: green")
        self.show_confirmation_window()
