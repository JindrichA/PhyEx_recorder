import cv2
import config
# Initialize the camera capture
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(config.cam_1)


# Loop to continuously read frames from the camera
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        break

    # Get the dimensions of the frame
    height, width = frame.shape[:2]

    # Calculate the center point of the image
    center_x = int(width / 2)
    center_y = int(height / 2)

    # Draw a cross at the center of the image
    cross_size = 50
    cross_thickness = 2
    cross_color = (0, 255, 0)
    cv2.line(frame, (center_x - cross_size, center_y), (center_x + cross_size, center_y), cross_color, cross_thickness)
    cv2.line(frame, (center_x, center_y - cross_size), (center_x, center_y + cross_size), cross_color, cross_thickness)

    # Display the frame with the cross
    cv2.imshow('Frame', frame)

    # Wait for a key press to exit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera capture and close the display window
cap.release()
cv2.destroyAllWindows()