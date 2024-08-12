# yolo scripts
目标检测、实例分割中常见的脚本:

1.yoloseg转成labelme：
yolo2labelme.py  

2.可视化yolo txt标签：
visualize_yolo_txt.py

3.yolov8 output0转换维度 [bs, xywh + classes + 32, 8400] -> [bs, 8400, xywh + classes + 32]：
v8trans.py

4.根据txt划分训练集、验证集：
split.py

5.labelme转coco:
labelme2coco.py

6.coco转yoloseg:
coco2yoloseg.py
