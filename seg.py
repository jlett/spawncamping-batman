###########################################################
#
#	Input: full page of doc
#	Output: array of single letter images
#	Next In Pileline: character recognition (Alberto)
#
###########################################################
import matplotlib.pyplot as plt

from skimage import img_as_float, io
from skimage.filter import threshold_otsu, threshold_adaptive


image = io.imread("testdoc.png");

block_size = 40
binary_adaptive = threshold_adaptive(image, block_size, offset=10)

fig, axes = plt.subplots(nrows=2, figsize=(7, 8))
ax0, ax1 = axes
plt.gray()

ax0.imshow(image)
ax0.set_title('Image')

ax1.imshow(binary_adaptive)
ax1.set_title('Adaptive thresholding')

for ax in axes:
    ax.axis('off')

plt.show()
