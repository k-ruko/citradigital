# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:10:35 2024

@author: k-ruko
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('C:/Users/k-ruko/Downloads/Vestia_Zeta_-_Portrait_01.webp',)
kernel = np.ones((5,5),np.uint8)

closing  = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

titles = [' Normal Image'   , ' closing ']
images = [image, closing,]

cv2.imshow("normal image", image)
cv2.imshow("closing", closing)

for i in range(7):
    plt.subplot(2,5,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()
cv2.waitKey(0)
cv2.destroyAllWIndows()