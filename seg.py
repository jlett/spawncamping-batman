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
from skimage import  data, novice, io, img_as_float
from skimage.filter import threshold_adaptive
from skimage.viewer import ImageViewer
import skimage.transform

img = img_as_float(io.imread("testdoc.png"))
#img = np.fix(img) #rounds values to nearest int

lx, ly = img.shape
xRES = int(lx/20) 
print(xRES)
yRES = int(ly/20)
print(yRES)

lowres = skimage.transform.resize(img, (xRES, yRES))

blackT = 40

img2 = np.copy(img)
img2[:lx/2, :] = 0

#for i in xrange(lx):
#	for j in xrange(ly):
#		val = np.rint(img[i, j])
i = 0
j = 0
for (i,j), value in np.ndenumerate(img):
	#print(i, j, img[i,j])
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
