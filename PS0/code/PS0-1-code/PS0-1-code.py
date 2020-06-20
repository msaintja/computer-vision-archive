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

#Checking that both images have been loaded correctly
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)) #openCV-matplotlib format fix
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

np.shape(img1) #images are 3-dimensional arrays

#Saving them
cv2.imwrite('./out/ps0-1-a-1.tiff', img1)
cv2.imwrite('./out/ps0-1-a-2.tiff', img2)
