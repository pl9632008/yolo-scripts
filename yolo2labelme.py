import os
import json
import base64
import numpy as np
from PIL import Image
import shutil



def img_to_b64(img_path):
    with open(img_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def convert_yolo_to_labelme(yolo_file, image_path, json_name=None, img_dst=None):
    if json_name is None:
        json_name = yolo_file.rstrip(".txt") + ".json"
    
    try:
        img = Image.open(image_path)
    except:
        return
    
    width, height = img.size

    data = {
        "version": "5.3.1",
        "flags": {},
        "shapes": [],
        "imagePath": os.path.basename(image_path),
        "imageData": img_to_b64(image_path),
        "imageHeight": height,
        "imageWidth": width,
    }

    with open(yolo_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split()
            cls = int(parts[0])
            pts = [float(x) for x in parts[1:]]
            
            
            shape = {
                "label": labels[cls],
                "line_color": None,
                "fill_color": None,
                "points": [[pts[i] * width, pts[i + 1] * height] for i in range(0, len(pts), 2)],  # rectangle represented as a polygon
                "shape_type": "polygon",
                "flags": {}
            }

            data["shapes"].append(shape)

    
    shutil.copy(image_path, img_dst)
    
    with open(json_name, "w") as json_outfile:
        json.dump(data, json_outfile, ensure_ascii=False, indent=2)


if __name__ == "__main__":

    labels = ["rail", "person", "car", "vehicle"]

    txt_path = r"E:\wjd\datasets_total_2024_8_1\val\labels"
    img_path = r"E:\wjd\datasets_total_2024_8_1\val\images"

    out_json_path = r"E:\wjd\testjson\jiangbei1coco\usedcoco\ceshi"


    if os.path.exists(out_json_path) == False:
        os.makedirs(out_json_path)

    txts = os.listdir(txt_path)

    for i in txts:
        
        txt = os.path.join(txt_path, i)

        img_name = i.replace(".txt",".jpg")
        img_out = os.path.join(img_path, img_name)
        img_dst = os.path.join(out_json_path, img_name)

        json_name = i.replace(".txt", ".json")
        json_out = os.path.join(out_json_path, json_name)

        convert_yolo_to_labelme(txt, img_out, json_out, img_dst)
