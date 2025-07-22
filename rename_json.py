import os
import json
import cv2
from labelme import utils
import shutil


prefix = "img7_"

path_dir = r"C:\Users\202311\Desktop\aaa\img7"

paths = os.listdir(path_dir)



for i in paths:
    b = i.split(".")

    if b[-1] == "json":
        json_path = os.path.join(path_dir,i)
        without_last = b[:-1]  

        img_name = ".".join(without_last)  # 使用逗号和空格作为分隔符
        img_name_ext = img_name + ".jpg"
        img_path = os.path.join(path_dir,img_name_ext)
        print(img_path)

        new_img_name = prefix+ img_name_ext
        new_img_path = os.path.join(path_dir, new_img_name)

        new_json_name = prefix + i
        new_json_path = os.path.join(path_dir,new_json_name)

        try:

            img = cv2.imread(img_path)
            
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            img_b64 = utils.img_arr_to_b64(img)  # 使用 LabelMe 工具函数
        except Exception as e:
            print(f"发生错误: {e}")
            continue

        data = None
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)  # 解析为Python字典/列表
            data["imageData"] = img_b64
            data["imagePath"] = prefix + img_name_ext

        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)  # 美化输出
        
        shutil.move(json_path, new_json_path)
        shutil.move(img_path, new_img_path)
