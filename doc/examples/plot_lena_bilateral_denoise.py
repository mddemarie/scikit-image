"""
====================================================
Denoising the picture of Lena using total variation
====================================================

In this example, we denoise a noisy version of the picture of Lena
using the total variation denoising filter. The result of this filter
is an image that has a minimal total variation norm, while being as
close to the initial image as possible. The total variation is the L1
norm of the gradient of the image, and minimizing the total variation
typically produces "posterized" images with flat domains separated by
sharp edges.

It is possible to change the degree of posterization by controlling
the tradeoff between denoising and faithfulness to the original image.

"""

import numpy as np
import matplotlib.pyplot as plt

from skimage import data, color, img_as_ubyte
from skimage.filter import tv_denoise
from skimage.rank import bilateral_mean
from skimage.morphology import disk

l = img_as_ubyte(color.rgb2gray(data.lena()))
l = l[230:290, 220:320]

noisy = l + 0.4 * l.std() * np.random.random(l.shape)

selem = disk(30)
bilateral_denoised = bilateral_mean(noisy.astype(np.uint8), selem=selem,s0=10,s1=10)

plt.figure(figsize=(8, 2))

plt.subplot(131)
plt.imshow(noisy, cmap=plt.cm.gray, vmin=40, vmax=220)
plt.axis('off')
plt.title('noisy', fontsize=20)
plt.subplot(132)
plt.imshow(bilateral_denoised, cmap=plt.cm.gray, vmin=40, vmax=220)
plt.axis('off')
plt.title('bilateral denoising', fontsize=20)

selem = disk(30)
bilateral_denoised = bilateral_mean(noisy.astype(np.uint8), selem=selem,s0=30,s1=30)
plt.subplot(133)
plt.imshow(bilateral_denoised, cmap=plt.cm.gray, vmin=40, vmax=220)
plt.axis('off')
plt.title('(more) bilateral denoising', fontsize=20)

plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0, left=0,
                    right=1)
plt.show()
