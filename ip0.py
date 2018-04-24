import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("ronaldo.jpg")
#plt.imshow(image)
#plt.show()
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()