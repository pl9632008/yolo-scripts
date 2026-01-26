import os
import random
import shutil
def split():
        path_dir = os.listdir(txt_dir)    #获取标签列表

        random.seed(8888)
        random.shuffle(path_dir)
        split_point = int(0.96   * len(path_dir))
 
        train_set = path_dir[:split_point]
        val_set = path_dir[split_point:]


        for text in train_set:
            name = os.path.splitext(text)[0]
            shutil.copy(os.path.join(txt_dir, text), os.path.join(train_txt, text) )
            shutil.copy(os.path.join(img_dir, name + ext), os.path.join(train_img, name + ext))

       
        for text in val_set:
            name = os.path.splitext(text)[0]
            shutil.copy(os.path.join(txt_dir, text), os.path.join(val_txt, text))
            shutil.copy(os.path.join(img_dir, name + ext),  os.path.join(val_img, name + ext))

        return



if __name__ == '__main__':

    ext = ".jpg" #默认图像的后缀

    # 基础路径
    base = r"E:\wjd\yolo_datasets_20251127_coco"

    # 拼接路径
    img_dir = os.path.join(base, "JPEGImages")
    txt_dir = os.path.join(base, "split")

    train_img = os.path.join(base, "dotrain", "train", "images")
    train_txt = os.path.join(base, "dotrain", "train", "labels")

    val_img = os.path.join(base, "dotrain", "val", "images")
    val_txt = os.path.join(base, "dotrain", "val", "labels")


    if os.path.exists(train_img) == False:
        os.makedirs(train_img)
    if os.path.exists(train_txt) == False:
        os.makedirs(train_txt)
    if os.path.exists(val_img) == False:
        os.makedirs(val_img)
    if os.path.exists(val_txt) == False:
        os.makedirs(val_txt)
    
    split()

