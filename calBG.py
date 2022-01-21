from os import write
from re import X
import cv2
import numpy as np

def create_gamma_img(gamma, img):
    gamma_cvt = np.zeros((256,1), dtype=np.uint8)
    for i in range(256):
        gamma_cvt[i][0] = 255*(float(i)/255)**(1.0/gamma)
    return cv2.LUT(img, gamma_cvt)

def BGx(img,y,x):
    sum = 0
    m = 2
    for i in y:
        for j in x:
            sum+=abs(img.item(i,j+m)-img.item(i,j))
    return sum

def BGy(img,y,x):
    sum = 0
    m = 2
    for i in y:
        for j in x:
            sum+=abs(img.item(i+m,j)-img.item(i,j))
    return sum

ROIpx = 80
ROIpy = 80 
#TAP1 = cv2.imread("G1_168.bmp",0)
#TAP2 = cv2.imread("G2_168.bmp",0)
#clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(3, 3))
TAP1 = cv2.medianBlur(cv2.imread("TAP1_168.jpg",0),5)
TAP2 = cv2.medianBlur(cv2.imread("TAP2_168.jpg",0),5)

ROI1 = TAP1[30:110,140:220]
ROI2 = TAP2[30:110,140:220]
ROI3 = TAP1[140:220,140:220]
ROI4 = TAP2[140:220,140:220]
cv2.rectangle(TAP1,(140,30),(140+ROIpx,30+ROIpy),(255, 255, 0))
cv2.rectangle(TAP1,(140,140),(140+ROIpx,140+ROIpy),(255,255,0))
cv2.rectangle(TAP2,(140,30),(140+ROIpx,30+ROIpy),(255, 255, 0))
cv2.rectangle(TAP2,(140,140),(140+ROIpx,140+ROIpy),(255,255,0))
cv2.imshow("TAP1",TAP1)
cv2.imshow("TAP2",TAP2)
cv2.imwrite("TAP1.jpg",TAP1)
cv2.imwrite("TAP2.jpg",TAP2)
print("BGx(TAP1Top)={}".format(BGx(TAP1,range(30,30+ROIpy),range(140,140+ROIpx))))
print("BGx(TAP2Top)={}".format(BGx(TAP2,range(30,30+ROIpy),range(140,140+ROIpx))))
print("BGx(TAP1Bottom)={}".format(BGx(TAP1,range(140,140+ROIpy),range(140,140+ROIpx))))
print("BGx(TAP2Bottom)={}".format(BGx(TAP2,range(140,140+ROIpy),range(140,140+ROIpx))))
print("BGy(TAP1Top)={}".format(BGy(TAP1,range(30,30+ROIpy),range(140,140+ROIpx))))
print("BGy(TAP2Top)={}".format(BGy(TAP2,range(30,30+ROIpy),range(140,140+ROIpx))))
print("BGy(TAP1Bottom)={}".format(BGy(TAP1,range(140,140+ROIpy),range(140,140+ROIpx))))
print("BGy(TAP2Bottom)={}".format(BGy(TAP2,range(140,140+ROIpy),range(140,140+ROIpx))))
cv2.waitKey(0)
cv2.destroyAllWindows()