# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:57:42 2024

@author: k-ruko
"""
#import cv2 dan numpy
import cv2
import numpy as np

#
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#if not cam.isOpened():
    #print("cant")
#melakukan while loop untuk menampilkan kamera setiap satu detik 
while True: 
    #mengubah masing masing citra sesuai dengan perintahnya
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (thresh,BW) = cv2.threshold(gray,155, 255,cv2.THRESH_BINARY)
    hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)
   
    
    #menampilkan citra kamera secara langsung 
    cv2.imshow("original", frame)
    cv2.imshow("Gray", gray)
    cv2.imshow("BW", BW)
    cv2.imshow("hsv", hsv)
    print("BW")
    print(BW)    
    print(hsv)
    print(gray)
    print(frame)

    if cv2.waitKey(1)==ord('1'):
        break
cv2.destroyAllWindows()