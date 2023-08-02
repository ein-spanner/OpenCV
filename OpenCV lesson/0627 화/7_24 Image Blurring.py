import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/fenor/image/logo.jpg')

blur = cv2.blur(img,(5,5))

plt.subplot(211), plt.imshow(img),plt.title('original')
plt.xticks([]), plt.yticks([])
plt.subplot(212),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
