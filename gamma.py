import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img3", 0)
i = 1
for gamma in [0.1 , 0.5 , 1.2 , 2.2]:
    gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype='uint8')
    plt.subplot(2 , 2 , i), plt.imshow(gamma_corrected , cmap='gray')
    plt.title(str(gamma))
    i = i + 1
plt.show()