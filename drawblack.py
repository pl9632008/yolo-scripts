#图像指定位置涂黑
import os
import cv2
import numpy as np

path = r"C:\Users\202311\Desktop\test_imgs"
path2 = r"C:\Users\202311\Desktop\test_imgs2"

a = os.listdir(path)

for i in a:
    b = i.split(".")

    if b[-1] == "jpg":

        img_path = os.path.join(path,i)

        img = cv2.imread(img_path)
        

        mask = np.ones(img.shape[:2], dtype=np.uint8) * 255

      
        points = np.array([[0,850],[0,1079],[45,1079],[918,338],[894,337]], np.int32)
        cv2.fillPoly(mask, [points], 0)

        img[mask == 0] = (0, 0, 0)

        new_img_path = os.path.join(path2,i)

        cv2.imwrite(new_img_path, img)

      
    
