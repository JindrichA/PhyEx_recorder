#
# cam1_filname = "rtsp://admin:kamera_fyzio_0" + str(1) + "@192.168.1.11" + str \
#     (1) + ":554/cam/realmonitor?channel=1&subtype=0"
# self.process_X = cammera
#
#     (
#     ffmpeg
#     .input(filename=cam1_filname)
#     .output
#         (filename=self.path_to_save_video s +self.name_of_the_exercis e +"_ " +self.utc_timestam p +"_ID_ " +self.ID_of_the_participan t +"_cam_ " +str
#             (1 ) +".mp4", c="copy")
#     .overwrite_output()
# )


class IP_Cam:
    def __init__(self, camera_number):
        self.camera_number = camera_number
        self.cam1_filname = "rtsp://admin:kamera_fyzio_0" + str(self.camera_number) + "@192.168.1.11" + str(self.camera_number) + ":554/cam/realmonitor?channel=1&subtype=0"
