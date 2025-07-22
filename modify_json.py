import os
import json
import cv2
from labelme import utils

path_dir = r"E:\wjd\yolo_datasets_20250716"

paths = os.listdir(path_dir)

for i in paths:
    b = i.split(".")

    if b[-1] == "json":
        json_path = os.path.join(path_dir,i)
        without_last = b[:-1]  

        img_name = ".".join(without_last)  # 使用逗号和空格作为分隔符
        img_name_ext = img_name + ".jpg"
        img_path = os.path.join(path_dir,img_name_ext)
        print("-------")
        print(img_path)
        print(json_path)
        print("-------")

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

        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)  # 美化输出
