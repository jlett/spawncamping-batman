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
import Image
from skimage import  data
from skimage.filter import threshold_adaptive
from skimage.viewer import ImageViewer
import skimage.transform

img = np.array(Image.open("testdoc.png"))

lx, ly = img.shape

lowres = skimage.transform.resize(img, (int(lx/20), int(ly/20)))

img2 = np.copy(img)
img2[:lx/2, :] = 0

for (i,j), value in np.ndenumerate(lowres):
	if value > 0.001:
		print(i, j, value)
	pass



#DISPLAY STUFF
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 5))
plt.gray()

ax[0].imshow(img)
ax[0].set_title("original")

ax[1].imshow(lowres)
ax[1].set_title("reduced resolution")

ax[2].imshow(img2)
ax[2].set_title("testimg")

plt.show()
