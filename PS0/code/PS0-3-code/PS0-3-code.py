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

).

# 3. Replacement of pixels

#Replacing inner 100 pixels square from one image by another
img1Mg = img1[:,:,1].copy() #BGR, green is the 2nd channel
img2Mg = img2[:,:,1].copy()

margin = (np.shape(img1Mg)[0] - 100) / 2 #both images are the same size
img1MgInner = img1Mg[margin:-margin, margin:-margin].copy()

img2MgRep = img2Mg.copy()
img2MgRep[margin:-margin, margin:-margin] = img1MgInner

cv2.imwrite('./out/ps0-3-a.tiff', img2MgRep)
plt.imshow(img2MgRep, cmap='gray', vmin = 0, vmax = 255)
