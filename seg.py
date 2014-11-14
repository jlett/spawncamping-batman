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

img = np.array(Image.open("testdoc.png").convert('L'))

lx, ly = img.shape

reducedRes = 10 #reduce resolution by factor of N
lowres = skimage.transform.resize(img, (int(lx/reducedRes), int(ly/reducedRes)))

minx, miny, maxx, maxy = (99999, 99999, 0, 0)
for (i,j), value in np.ndenumerate(lowres):
	if value < 1.0:
		if i < minx:
			minx = i
		if j < miny:
			miny = j
		if i > maxx:
			maxx = i
		if j > maxy:
			maxy = j		

cropped = img[minx*reducedRes:maxx*reducedRes, miny*reducedRes:maxy*reducedRes]

#DISPLAY STUFF
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 5))
plt.gray()

ax[0].imshow(img)
ax[0].set_title("original")

ax[1].imshow(lowres)
ax[1].set_title("reduced resolution")

ax[2].imshow(cropped)
ax[2].set_title("cropped")

plt.show()
