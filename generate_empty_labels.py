import os
import argparse

def create_empty_txt_for_images(img_dir, label_dir):
    """为没有标签文件的图片创建空白txt（支持不同目录）"""
    # 支持的图片扩展名列表
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    
    # 确保标签目录存在
    os.makedirs(label_dir, exist_ok=True)
    
    # 遍历图片目录中的所有文件
    for img_filename in os.listdir(img_dir):
        # 检查是否是图片文件
        if any(img_filename.lower().endswith(ext) for ext in image_extensions):
            # 获取图片基本名（不含扩展名）
            base_name = os.path.splitext(img_filename)[0]
            # 构造对应的标签文件路径
            txt_path = os.path.join(label_dir, base_name + '.txt')
            
            # 如果不存在对应的txt文件
            if not os.path.exists(txt_path):
                # 创建空白txt文件
                with open(txt_path, 'w') as f:
                    pass  # 创建空文件
                print(f"创建空白标签: {os.path.basename(txt_path)}")
            # 可选：显示已存在标签的文件
            else:
                print(f"标签已存在: {os.path.basename(txt_path)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='为没有标签的图片生成空白txt文件')
    parser.add_argument('--img-dir', type=str, required=True, 
                        help='图片目录路径')
    parser.add_argument('--label-dir', type=str, required=True,
                        help='标签目录路径')
    
    args = parser.parse_args()
    
    create_empty_txt_for_images(args.img_dir, args.label_dir)
    print(f"空白标签生成完成！检查目录: {args.label_dir}")
