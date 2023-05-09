import cv2
import time
import config
# Initialize the camera captures
cap1 = cv2.VideoCapture(config.cam_4)
cap2 = cv2.VideoCapture(config.cam_3)
cap3 = cv2.VideoCapture(config.cam_4)
cap4 = cv2.VideoCapture(config.cam_4)

# Set the frame size for all cameras
# frame_width = 320
# frame_height = 240
# cap1.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
# cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
# cap2.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
# cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

# cap3.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
# cap3.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
# cap4.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
# cap4.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

# Loop to continuously switch views between cameras every second
while True:
    # Read a frame from each camera
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    # ret3, frame3 = cap3.read()
    # ret4, frame4 = cap4.read()
    frame1 = cv2.resize(frame1, (int(frame1.shape[1] / 2), int(frame1.shape[0] / 2)))
    frame2 = cv2.resize(frame2, (int(frame2.shape[1] / 2), int(frame2.shape[0] / 2)))
    frame_height = frame1.shape[0]
    frame_width = frame1.shape[1]
    # Check if all frames were successfully read
    if not (ret1 and ret2):
        break

    # Add a cross to each frame at the center
    center_x = int(frame_width / 2)
    center_y = int(frame_height / 2)

    cross_size = 50
    cross_thickness = 2
    cross_color = (0, 255, 0)
    cv2.line(frame1, (center_x - cross_size, center_y), (center_x + cross_size, center_y), cross_color, cross_thickness)
    cv2.line(frame1, (center_x, center_y - cross_size), (center_x, center_y + cross_size), cross_color, cross_thickness)
    cv2.line(frame2, (center_x - cross_size, center_y), (center_x + cross_size, center_y), cross_color, cross_thickness)
    cv2.line(frame2, (center_x, center_y - cross_size), (center_x, center_y + cross_size), cross_color, cross_thickness)


    # Display the frames in a grid
    grid = cv2.vconcat([cv2.hconcat([frame1, frame2]), cv2.hconcat([frame1, frame2])])
    cv2.imshow('Grid', grid)
    cv2.waitKey(1)