# Importing the opencv library for Python
import cv2
# Importing numpy for matrices/images handling
import numpy as np
# Importing matplotlib.pyplot to embed images within this notebook
import matplotlib.pyplot as plt

# 1. Input images

# Loading the 2 images downloaded 
# from http://sipi.usc.edu/database/database.php?volume=misc
img1 = cv2.imread('./images/4.2.06.tiff', cv2.IMREAD_COLOR)
img2 = cv2.imread('./images/4.2.07.tiff', cv2.IMREAD_COLOR)

img1Mg = img1[:,:,1].copy() #BGR, green is the 2nd channel

# 4. Arithmetic and Geometric operation

# a. min, max, mean, standard deviation
print np.min(img1Mg), np.max(img2Mg), np.mean(img1Mg), np.std(img1Mg)

# The minimum and maximum pixel intensity values for the monochrome version of Image 1 are 0 and 237. The average is about 124 and the standard deviation, about 78. These values were obtained using Numpy's built-in vectorized methods.

# b. Operations on the monochrome image with mean and std.
img1MgMeanStd = (img1Mg - np.mean(img1Mg))/np.std(img1Mg) * 10 + np.mean(img1Mg)
cv2.imwrite('./out/ps0-4-b.tiff', img1MgMeanStd)
plt.imshow(img1MgMeanStd, cmap='gray', vmin = 0, vmax = 255)

# c. Shifting the image by 2 pixels
img1MgShift = np.roll(img1Mg, shift = -2, axis = 1)
cv2.imwrite('./out/ps0-4-c.tiff', img1MgShift)
plt.imshow(img1MgShift, cmap='gray', vmin = 0, vmax = 255)

# d. Substracting the shifted image to the original
img1MgDiff = img1Mg - img1MgShift

img1MgDiff[img1MgDiff < 0] = 0
cv2.imwrite('./out/ps0-4-d.tiff', img1MgDiff)
plt.imshow(img1MgDiff, cmap='gray', vmin = 0, vmax = 255)