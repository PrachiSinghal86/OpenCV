# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:02:43 2019

@author: user
"""

import cv2
import numpy as np

cap=cv2.VideoCapture(0) #webcam
#cap=cv2.VideoCapture('output.avi') ##to load a video
forcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',forcc,20.0,(640,480))
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('Gray',gray)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


