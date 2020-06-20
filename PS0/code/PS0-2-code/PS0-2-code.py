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


# 2. Color planes

# a. Swap the red and blue pixels of image 1
img1brswap = img1.copy()

red_ch = img1brswap[:,:,2].copy() #BGR, red is the 3rd channel
blue_ch = img1brswap[:,:,0].copy() #BGR, blue is the 1st channel

img1brswap[:,:,2] = blue_ch
img1brswap[:,:,0] = red_ch
cv2.imwrite('./out/ps0-2-a.tiff', img1brswap)
plt.imshow(cv2.cvtColor(img1brswap, cv2.COLOR_BGR2RGB))

# b. Monochrome image from image 1, using only the green channel
img1Mg = img1[:,:,1].copy() #BGR, green is the 2nd channel

cv2.imwrite('./out/ps0-2-b.tiff', img1Mg)
plt.imshow(img1Mg, cmap='gray', vmin = 0, vmax = 255) # prevent plt rescale

# c. Monochrome image from image 1, using only the red channel
img1Mr = img1[:,:,2].copy() #BGR, red is the 3rd channel

cv2.imwrite('./out/ps0-2-c.tiff', img1Mr)
plt.imshow(img1Mr, cmap='gray', vmin = 0, vmax = 255)

# d.  
# The image obtained from extracting the green channels seems to be closer to what I would expect a monochrome image to look like. The contrast and distinction between black and white parts are more accentuated, comparatively to the other image (using the red channel). In the second case, it seems like everything is closer to an in-between value, moderately grey.  
# While it depends on what kind of algorithms we are looking to use and what goal we are pursuing, I think the green-channel one would be more useful when contrasts (or intensity differences) are important (e.g. identifying different zones of an image).
