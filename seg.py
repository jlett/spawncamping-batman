###########################################################
#
#	Input: full page of doc assumed with no extra noise or deformations
#	Output: array of single letter images
#	Previous in Pipeline: denoise and island removal (Jack)
#	Next In Pileline: character recognition (Alberto)
#
###########################################################
import matplotlib.pyplot as plt
import numpy as np
import skimage
from skimage import  data, io, img_as_float
from skimage.filter import threshold_adaptive
from skimage.viewer import ImageViewer

img = img_as_float(io.imread("testdoc.png"))

lx, ly = img.shape
cropped = img[lx / 4: - lx / 4, ly / 4: - ly / 4]

#histo = np.histogram(img, bins=np.arange(0, 256))

#block_size = 40
#binary_adaptive = threshold_adaptive(img, block_size, offset=10)



#DISPLAY STUFF
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 5))
plt.gray()

ax[0].imshow(img)
ax[0].set_title("original")

#ax[0, 1].imshow(histo)
#ax[0, 1].set_title("histogram")

ax[1].imshow(cropped)
ax[1].set_title("cropped")

plt.show()
