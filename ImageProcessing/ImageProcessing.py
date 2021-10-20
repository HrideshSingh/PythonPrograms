'''
#Flipping the Image

from PIL import Image

#opening the image
img=Image.open('ImageProcessing/board.jpg')

#transposing
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

#Save it to a file in a human understandable format
transposed_img.save('corrected.jpg')

print('Done flipping')

'''

#Image Enchancement Technique

import cv2

#read the image

img=cv2.imread('ImageProcessing/board.jpg')

#Preaperation for CLAME

clahe =cv2.createCLAHE()

#Convert to gray Scale Image

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Apply enchancement

enh_img = clahe.apply(gray_img)

#saved in a file 
cv2.imwrite('enhanced.jpg',enh_img)

print('Done enchancing')


