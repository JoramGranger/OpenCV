import os

import cv2

img = cv2.imread(os.path.join('.', 'data', 'rally.jpg'))

k_size = 11
img_blur =cv2.blur(img, (k_size, k_size))
img_g_blur = cv2.GaussianBlur(img, (k_size, k_size), 5)
img_m_blur = cv2.medianBlur(img, k_size)
                              
cv2.imshow('img', img)
cv2.imshow('img', img_blur)
cv2.imshow('img', img_g_blur)
cv2.imshow('img', img_m_blur)
cv2.waitKey(0)