import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("img4")
image = cv2.resize(image , (500, 600))

image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

clahe = cv2.create.apply(image_bw) + 30

_, ordinary_img = cv2.thresold(image_bw, 155, 2555, cv2.THRESH_BINARY)

plt.subplot(2, 2, 2), plt.imshow(iamge, cmap='gray')
plt.title('origianl'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2), plt.imshow(iamge, cmap='gray')
plt.title('ordinary thresold'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2), plt.imshow(iamge, cmap='gray')
plt.title('clahe image'), plt.xticks([]), plt.yticks([])