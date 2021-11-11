# Author : Dongyoon Kim
# Description : Apply Canny Lane Detection Algorithm

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2.cv2 as cv2

image = mpimg.imread('exit-ramp.jpg')
plt.imshow(image)
plt.show()

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # grayscale conversion
plt.imshow(gray, cmap='gray')
plt.show()

# Let's try Canny edge detector algorithm
# Input : image, low_thres, high_thres
edges = cv2.Canny(gray,)
