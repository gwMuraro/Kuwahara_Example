import cv2
from pykuwahara import kuwahara

image = cv2.imread('montagne.jpg')
filt2 = kuwahara(image, method='gaussian', radius=9)

cv2.imshow(filt2)
