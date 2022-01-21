from os import write
import cv2
import numpy as np
import csv
 
def create_gamma_img(gamma, img):
    gamma_cvt = np.zeros((256,1), dtype=np.uint8)
    for i in range(256):
        gamma_cvt[i][0] = 255*(float(i)/255)**(1.0/gamma)
    return cv2.LUT(img, gamma_cvt)



Gate1 = cv2.imread('G1_000.bmp',0)


Gate2 = cv2.imread('G2_000.bmp',0)

img_diff = cv2.absdiff(Gate2, Gate1)
diff_gamma = create_gamma_img(1.5, img_diff)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img_diff)

print(min_val)
print(f"max:{max_val},loc:{max_loc}")
with open('gate1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(Gate1)
f.close()
with open('gate2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(Gate2)
f.close()
with open('gate_diff.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(img_diff)
f.close()

cv2.imshow('diff',img_diff)
cv2.imshow('gate1',Gate1)
cv2.imshow('gate2',Gate2)
cv2.imshow('diffganma',diff_gamma)
cv2.imwrite('Gata2-Gate1_diff.bmp', img_diff)
cv2.imwrite('Gata2-Gate1_diff_gamma.bmp', diff_gamma)
cv2.waitKey(0)
cv2.destroyAllWindows()