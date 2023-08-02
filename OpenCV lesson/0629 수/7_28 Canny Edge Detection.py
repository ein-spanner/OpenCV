import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/fenor/image/timetable.png',0)
edges = cv2.Canny(img,30,200)

plt.subplot(211),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(212),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
