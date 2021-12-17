# -*- coding: utf-8 -*-
"""filtiring_masks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18nkjr__3SwvFMzDSpVcurVromA-TaOUE
"""

# Commented out IPython magic to ensure Python compatibility.
import cv2
import glob
from PIL import Image
import os
import numpy as np
import imageio
from PIL import Image
import cv2
from nibabel.testing import data_path
example_filename = os.path.join(data_path, '/content/coronacases_002.nii')
import nibabel as nib
img = nib.load(example_filename)
img.shape
import matplotlib.pyplot as plt
# %matplotlib inline

img.shape[2]

img.get_data_dtype() == np.dtype(np.int16)

img.affine.shape

a= np.array(img.dataobj[:, :, 100])

a.shape

a

type(a)

image = cv2.rotate(a, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

plt.gray()
plt.imshow(image)

for i in range (img.shape[2]):
     a= np.array(img.dataobj[:, :, i])
     image = cv2.rotate(a, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)  
     result = np.all((a == 0))
     if result:
         continue
     else:
          name = 'corona' + str(i) + '.png'
          plt.imsave(name, image)