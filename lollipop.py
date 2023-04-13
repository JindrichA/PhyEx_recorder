import cv2
import numpy as np
import random

# Define the color of the lollipops
LOLLIPOP_COLOR = (255, 0, 0)  # blue color

# Define the color of the lollipop sticks
STICK_COLOR = (0, 255, 0)  # green color

# Define the number of lollipops to generate
NUM_LOLLIPOPS = 30

# Define the size of the lollipops
LOLLIPOP_SIZE = 30

# Define the size of the lollipop sticks
STICK_WIDTH = 10
STICK_HEIGHT = 100

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video capture")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Main loop
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if frame is read correctly
    if not ret:
        print("Error reading frame")
        break

    # Generate lollipops randomly on the frame
    for i in range(NUM_LOLLIPOPS):
        x = random.randint(0, frame.shape[1] - LOLLIPOP_SIZE)
        y = random.randint(0, frame.shape[0] - LOLLIPOP_SIZE - STICK_HEIGHT)
        center = (x + LOLLIPOP_SIZE // 2, y + LOLLIPOP_SIZE // 2)
        # Draw lollipop stick
        stick_start = (center[0], center[1] + LOLLIPOP_SIZE // 2)
        stick_end = (stick_start[0], stick_start[1] + STICK_HEIGHT)
        cv2.line(frame, stick_start, stick_end, STICK_COLOR, STICK_WIDTH)
        # Draw lollipop
        cv2.circle(frame, center, LOLLIPOP_SIZE // 2, LOLLIPOP_COLOR, -1)

    # Write the augmented frame to the output video file
    out.write(frame)

    # Display the augmented frame
    cv2.imshow('Lollipop Rain Simulation', frame)

    # Wait for key press to exit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture and writer objects
cap.release()
out.release()

# Close all windows
cv2.destroyAllWindows()
