# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 23:23:30 2024

@author: k-ruko
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread("C:/Users/k-ruko/Downloads/Vestia_Zeta_-_Portrait_01.webp")
image1 = cv2.imread('C:/Users/k-ruko/Downloads/dancing_cow.webp', )
image2 = cv2.imread('C:/Users/k-ruko/Downloads/sucipto.jfif', )



#morfologi#
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(image,kernel,iterations = 1)
dilation = cv2.dilate(image,kernel,iterations = 1)
opening = cv2.morphologyEx(image1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(image2, cv2.MORPH_CLOSE, kernel)

print (image.shape) 

cv2.resize(image, (200,300))
cv2.resize(erosion, (300,300))
cv2.resize(dilation, (300,300))
cv2.resize(opening, (300,300))
cv2.resize(closing, (300,300))


titles = [' Normal Image', ' Erosion ',
          ' Dilation ', ' Before Opening ', 
          ' Opening ', 'Before Closing ', ' Closing '  ]

images = [image, erosion, dilation, image1, opening, image2, closing]

cv2.imshow("image", image)
cv2.imshow("erosion", erosion)
cv2.imshow("dilatation", dilation)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)


for i in range(7):
    plt.subplot(2,5,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()
cv2.waitKey(0)
cv2.destroyAllWIndows()
