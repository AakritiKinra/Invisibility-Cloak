from cv2 import cv2
import numpy as np
import time

camera=cv2.VideoCapture(0)
time.sleep(5)
background=0

ret,background=camera.read()
background=np.flip(background,axis=1)
while (camera.isOpened()):
    ret,image=camera.read()
    image=np.flip(image,axis=1)

    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    blurred=cv2.GaussianBlur(hsv,(35,35),0)

    lower=np.array([0,120,70])
    upper=np.array([10,255,255])
    mask_1=cv2.inRange(hsv,lower,upper)

    lower_red=np.array([170,120,705])
    upper_red=np.array([180,255,255])
    mask_2=cv2.inRange(hsv,lower_red,upper_red)

    mask=mask_1+mask_2
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
    
    image[np.where(mask==255)]=background[np.where(mask==255)]
    cv2.imshow('Display',image)
    
    if cv2.waitKey(1)==27:
        break