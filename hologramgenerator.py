# -*- coding: utf-8 -*-
"""HologramGenerator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bopy4fNDoEs_6vhiDF4iZNQ3pthFanuh
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:39:13 2023
Purpose: To create a hologram image
@author: Achintha Aththanayake
"""

#import libraries
import cv2
import numpy as np
import glob #used to search files that match specific file or name

#create a list to append edited images
img_array = []

#create canvas
h, w, c = img.shape
bg_img_w = int(w * 0.5 * 3)
bg_img_h = int(h * 0.5 * 3)
bg_img = np.zeros((bg_img_w, bg_img_h, c), dtype = "uint8")
cv2.imshow('Background', bg_img)

#get the images in the folder
for filename in glob.glob('C:/New folder/Images/*.jpg'):
  #filename = "cover2.jpg"
  img = cv2.imread(filename)

  #call image rotation and scaling functions
  x_scl_prec, y_scl_prec = 0.5, 0.5
  img_Top, img_Left, img_Bottom, img_Right = rot_Scaler(img, x_scl_prec, y_scl_prec)

  #create hologram image
  img = holo_Image(bg_img, scaler_W, scaler_H, img_Top, img_Left, img_Bottom, img_Right)

  #Append edited image to the image list
  img_array.append(img)

#Transfer image list images to a video
for i in range(len(img_array)):
     out.write(img_array[i])

#Release video writer
out.release()