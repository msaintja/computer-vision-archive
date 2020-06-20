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


# ## 5. Noise

# a. Adding gaussian noise
sigma = 5

noise = np.zeros_like(img1)
noise[:,:,1] = np.random.standard_normal(np.shape(img1)[0:2]) * sigma
img1Noisy = img1 + noise
img1Noisy[img1Noisy < 0] = 0
img1Noisy[img1Noisy > 255] = 255

img1Noisy = img1Noisy
cv2.imwrite('./out/ps0-5-a.tiff', img1Noisy)
plt.imshow(cv2.cvtColor(img1Noisy, cv2.COLOR_BGR2RGB))

# The noise was visible starting from sigma = 1, but I've increased it a bit (5) to have noise present in different areas.

# b. Adding gaussian noise
sigma = 5

noise_blue = np.zeros_like(img1)
noise_blue[:,:,0] = np.random.standard_normal(np.shape(img1)[0:2]) * sigma
img1NoisyBlue = img1 + noise_blue
img1NoisyBlue[img1NoisyBlue < 0] = 0
img1NoisyBlue[img1NoisyBlue > 255] = 255

img1Noisy = img1Noisy
cv2.imwrite('./out/ps0-5-b.tiff', img1NoisyBlue)
plt.imshow(cv2.cvtColor(img1NoisyBlue, cv2.COLOR_BGR2RGB))


# c.  
# In this case, for this image and this amount of noise, the blue noise doesn't affect the image as the green noise. As the noise on the green channel happens to be very visible (green becomes prevalent over other channels) in dark areas (where the contrast is important), it is more difficult to perceive a difference with noise on the blue channel. Hence, the second image looks better.
