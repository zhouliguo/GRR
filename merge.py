import cv2
import numpy as np

image1 = cv2.imread('results/dark.png')
image2 = cv2.imread('results/dfd.png')
image3 = cv2.imread('results/mafa.png')

h = image1.shape[0]
if h > image2.shape[0]:
    h = image2.shape[0]
if h > image3.shape[0]:
    h = image3.shape[0]

w1 = int(h/image1.shape[0]*image1.shape[1])
w2 = int(h/image2.shape[0]*image2.shape[1])
w3 = int(h/image3.shape[0]*image3.shape[1])

image1 = cv2.resize(image1,(w1,h))
image2 = cv2.resize(image2,(w2,h))
image3 = cv2.resize(image3,(w3,h))

image = np.ones((h, w1+8+w2+8+w3, 3), np.uint8)*255

image[:,:w1] = image1
image[:,w1+8:w1+8+w2] = image2
image[:,w1+8+w2+8:] = image3

cv2.imwrite('ddm.png', image)

cv2.imshow('image', image)
cv2.waitKey()


