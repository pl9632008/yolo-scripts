import cv2
import numpy as np
import glob
import os
import shutil

# path
pic_path = r"E:\wjd\testjson\jiangbei1coco\usedcoco\JPEGImages"

txt_path = r"E:\wjd\testjson\jiangbei1coco\usedcoco\split"

out_path = r"E:\wjd\testjson\jiangbei1coco\usedcoco\visualyolo"

if os.path.exists(out_path) == False:
    os.makedirs(out_path)


pic = os.listdir(pic_path)

for i in pic:

    pic_file = os.path.join(pic_path, i)

    img = cv2.imread(pic_file)

    substrings = pic_file.split('\\')[-1]

    last_dot_index = substrings.rfind('.')
    

    if last_dot_index != -1:
        result_string = substrings[:last_dot_index]
    else:
        result_string = substrings  


    height, width, _ = img.shape

    txt_file = os.path.join(txt_path, result_string   + ".txt")

    # file_handle = open(txt_file)

    try:
        file_handle = open(txt_file)
    except:
          os.remove(pic_file)
          continue

    cnt_info = file_handle.readlines()
    new_cnt_info = [line_str.replace("\n", "").split(" ") for line_str in cnt_info]
 
    for new_info in new_cnt_info:
        s = []
        for i in range(1, len(new_info), 2):
            b = [float(tmp) for tmp in new_info[i:i + 2]]
            s.append([int(b[0] * width), int(b[1] * height)])
        class_ = new_info[0]
        index = int(class_)
        cv2.polylines(img, [np.array(s, np.int32)], True, (0,255,255), thickness = 3)
        cv2.putText(img, class_, s[0],cv2.FONT_HERSHEY_SIMPLEX,2, (255,255,0) ,3)
 

    save_path = os.path.join(out_path,result_string + '.jpg')

    cv2.imwrite(save_path, img)