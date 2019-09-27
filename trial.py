# trial.py
# this version records the cam input from the webcam and creates a high
# frequency search of edge detection


import cv2 as cv
import numpy as np
import imutils


# initialize the camera
cam = cv.VideoCapture(0)   # 0 -> index of camera


while (1):
    s, img = cam.read()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    thrs1 = cv.getTrackbarPos('thrs1', 'edge')
    thrs2 = cv.getTrackbarPos('thrs2', 'edge')
    edge = cv.Canny(gray, thrs1, thrs2, apertureSize=5)
    vis = img.copy()
    vis = np.uint8(vis/2.)
    vis[edge != 0] = (0, 255, 0)
    
    cv.imshow('edge', vis)
    cv.waitKey(1)
