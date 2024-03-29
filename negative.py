import cv2
import matplotlib.pyplot as plt
img_bgr = 1 - img_bgr
gray =cv2.imread('img3' , 0)
gray_negative = abs(255-gray)
imgs = [img_bgr, gray, img_neg , gray_negative]
title = ['colorued', 'gray', 'colorued_negative', 'gray_negative']

plt.subplot(2, 2, 2), plt.title(title[1])
plt.imshow(imgs[1], cmap='gray'), plt.xticks(([]), plt.yticks([]))

plt.subplot(2, 2, 3), plt.title(title[1])
plt.imshow(imgs[2]), plt.xticks(([]), plt.yticks([]))

plt.subplot(2, 2, 4), plt.title(title[1])
plt.imshow(imgs[3], cmap='gray'), plt.xticks(([]), plt.yticks([]))

plt.show()