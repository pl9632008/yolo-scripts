import os
import random
import shutil
def split():
        path_dir = os.listdir(txt_dir)    #获取标签列表
   
        random.shuffle(path_dir)
        split_point = int(0.8 * len(path_dir))
 
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

    img_dir = r"D:\split_json_coco\JPEGImages" #原始图像文件夹
    txt_dir = r"D:\split_json_coco\split" #原始txt文件夹
    
    train_img = r"D:\split_json_coco\train_img"#划分train图像文件夹
    train_txt = r"D:\split_json_coco\train_txt"#划分train_txt文件夹

    val_img =r"D:\split_json_coco\val_img"    #划分val图像文件夹
    val_txt = r"D:\split_json_coco\val_txt" #划分val_txt文件夹

    if os.path.exists(train_img) == False:
        os.makedirs(train_img)
    if os.path.exists(train_txt) == False:
        os.makedirs(train_txt)
    if os.path.exists(val_img) == False:
        os.makedirs(val_img)
    if os.path.exists(val_txt) == False:
        os.makedirs(val_txt)
    
    split()

