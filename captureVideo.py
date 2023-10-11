import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
# green = np.array([[0, 255, 0]], dtype=np.uint8)
# hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
# lowerBound = np.array([hsv_green[0][0][0] - 10, 100, 100], dtype=np.uint8)
# upperBound = np.array([hsv_green[0][0][0] + 10, 255, 255], dtype=np.uint8)
# pink_rgb = 255, 192, 203
# pink_hsv = 175, 63, 255

# lowerGreen = np.array([50, 100, 100], dtype=np.uint8)
# upperGreen = np.array([70, 255, 255], dtype=np.uint8)

lowerPink = np.array([165, 100, 100], dtype=np.uint8)
upperPink = np.array([185, 255, 255], dtype=np.uint8)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Threshold the HSV image to get only pink colors
    mask = cv.inRange(hsv, lowerPink, upperPink)

    # Bounding Rectangle
    x, y, w, h = cv.boundingRect(mask)
    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
