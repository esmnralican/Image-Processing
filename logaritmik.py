import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("img6")

c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))

log_image = np.array(log_image, dtype=np.uint8)

plt.subplot(1, 2, 1), plt.show(image)
plt.title('original')
plt.subplot(1, 2, 1), plt.imshow(log_image)
plt.title('logaritmik')
plt.show()