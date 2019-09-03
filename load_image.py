# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:34:21 2019

@author: user
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
#for gray scale use IMREAD_GRAYSCALE

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#draws a red line between 2 points
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot([60,100],[80,100],'r',linewidth=5)
plt.show()

cv2.imwrite('watchgray.png',img)
