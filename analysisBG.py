from os import write
from re import X
import cv2
import numpy as np

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
F = []
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(3, 3))

for i in range(1,500):
    #TAP1 = clahe.apply(cv2.imread(f"C:\\Users\\kuro-\\Documents\\pgmAnalysis\\TAP1\\image{i:03}.jpg",0))
    #TAP2 = clahe.apply(cv2.imread(f"C:\\Users\\kuro-\\Documents\\pgmAnalysis\\TAP2\\image{i:03}.jpg",0))
    TAP1 = cv2.imread(f"C:\\Users\\kuro-\\Documents\\pgmAnalysis\\TAP1\\image{i:03}.jpg",0)
    TAP2 = cv2.imread(f"C:\\Users\\kuro-\\Documents\\pgmAnalysis\\TAP2\\image{i:03}.jpg",0)

    F.append({"Frame":i,
    "BGx(TAP1Top)":BGx(TAP1,range(30,30+ROIpy),range(140,140+ROIpx)),
    "BGx(TAP2Top)":BGx(TAP2,range(30,30+ROIpy),range(140,140+ROIpx)),
    "BGx(TAP1Bottom)":BGx(TAP1,range(140,140+ROIpy),range(140,140+ROIpx)),
    "BGx(TAP2Bottom)":BGx(TAP2,range(140,140+ROIpy),range(140,140+ROIpx)),
    "BGy(TAP1Top)":BGy(TAP1,range(30,30+ROIpy),range(140,140+ROIpx)),
    "BGy(TAP2Top)":BGy(TAP2,range(30,30+ROIpy),range(140,140+ROIpx)),
    "BGy(TAP1Bottom)":BGy(TAP1,range(140,140+ROIpy),range(140,140+ROIpx)),
    "BGy(TAP2Bottom)":BGy(TAP2,range(140,140+ROIpy),range(140,140+ROIpx))
    })


for i in F:
    if (i["BGx(TAP2Top)"]>i["BGx(TAP1Top)"]) and i["BGx(TAP1Bottom)"]>i["BGx(TAP2Bottom)"]>4000:
        print(i) 

