import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'rally.jpg'))


cropped_img = img[320:640, 420:840]

print(img.shape)
print(cropped_img.shape)

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)