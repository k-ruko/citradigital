# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 00:23:09 2024

@author: k-ruko
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

def showHistogramRGB(image, title):
    # Mengambil masing-masing warna merah, hijau dan biru dari citra
    red, green, blue = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    red = red.flatten()
    green = green.flatten()
    blue = blue.flatten()
    # Memasukkan data warna merah, hijau, dan biru ke plot
    plt.hist(red, bins=256, density=False, color='red', alpha=0.5)
    plt.hist(green, bins=256, density=False, color='green', alpha=0.4)
    plt.hist(blue, bins=256, density=False, color='blue', alpha=0.3)
    plt.title(title)
    plt.show()

def showHistogram(image, title):
    # Mengambil nilai mean dari warna biru
    image = image.mean(axis=2).flatten()
    plt.hist(image, bins=256, density=False, color='black')
    plt.title(title)
    plt.show()

img = cv2.imread("C:/Users/k-ruko/Downloads/640px-Kobo_Kanaeru_-_Portrait_01.webp")
average = cv2.blur(img,(3,3))
gaussian = cv2.GaussianBlur(img,(3,3),0)
median = cv2.medianBlur(img,3)

kernelLPF = np.array([[0, 1/8, 0],[1/8, 1/2, 1/8],[0, 1/8, 0]],np.float32)
kernelHPF = np.array([[-1/9, -1/9, -1/9],[-1/9, 8/9, -1/9],[-1/9, -1/9, -1/9]],np.float32)

# Konvolusi citra
LPF = cv2.filter2D(img, -1, kernelLPF)
HPF = cv2.filter2D(img, -1, kernelHPF)

images = [img, average, gaussian, median, LPF, HPF]
titles = ["Original", "Averaging", "Gaussian Blur", "Median Blur", "Low Pass Filter", " High Pass Filter"]

for i in range(len(images)):
    showHistogram(images[i], titles[i])

for i in range(len(images)):
    showHistogramRGB(images[i], titles[i])
for i in range(len(images)):
    cv2.imshow(titles[i], images[i])
cv2.waitKey(0)
cv2.destroyAllWindows()
