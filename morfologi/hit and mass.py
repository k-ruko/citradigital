# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:36:33 2024

@author: k-ruko
"""

import cv2 as cv
import numpy as np
 
input_image = np.array((
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 255, 255, 0, 0, 0, 255],
    [0, 0, 255, 255, 0, 0, 0, 0],
    [0, 0, 255, 255, 0, 255, 0, 0],
    [0, 0, 255, 0, 0, 255, 0, 0],
    [0, 0, 255, 0, 0, 255, 255, 0],
    [0,255, 0, 255, 0, 255, 0, 0],
    [0, 255, 255, 255, 0, 0, 0, 0]), dtype="uint8")
 
kernel = np.array((
        [0, 1, 0],
        [1, -1, 1],
        [0, 1, 0]), dtype="int")
 
out_img = cv.morphologyEx(input_image, cv.MORPH_HITMISS, kernel)
 
rate = 50
kernel = (kernel + 1) * 127
kernel = np.uint8(kernel)
 
kernel = cv.resize(kernel, None, fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
cv.imshow("kernel1", kernel)
cv.moveWindow("kernel", 0, 0)
 
input_image = cv.resize(input_image, None, fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
cv.imshow("Original1", input_image)
cv.moveWindow("Original", 0, 200)
 
out_img = cv.resize(out_img, None , fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
cv.imshow("Hit or Miss1", out_img)
cv.moveWindow("Hit or Miss", 500, 200)
 
cv.waitKey(0)
cv.destroyAllWindows()
