import cv2 as cv
import numpy as np

cap = cv.VideoCapture('rtsp://admin:pass@192.168.1.108:554/cam/realmonitor?channel=1&subtype=02&authbasic=xxxxxxxx')

while(True):
    ret, frame = cap.read()
    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
