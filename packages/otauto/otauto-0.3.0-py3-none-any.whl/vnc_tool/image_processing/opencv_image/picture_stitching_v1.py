import cv2
import os
from datetime import datetime
import numpy as np
"""
功能:图片拼接
更新日志:2024-11-12 12:42:20
拼接成灰度图
"""

# 获取当前时间
current_time = datetime.now()

# 格式化时间
formatted_time = current_time.strftime('%Y-%m-%d %H%M%S')

def stitch_images(images):
    """拼接图片"""
    # 创建一个Stitcher对象
    stitcher = cv2.Stitcher_create()

    # 拼接图像
    status, stitched_image = stitcher.stitch(images)

    if status != cv2.Stitcher_OK:
        print("Error stitching images, status code:", status)
        return None
    return stitched_image

def load_images_from_folder(folder):
    """从文件夹内加载图片"""
    images = []
    for filename in sorted(os.listdir(folder)):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            img = cv2.imdecode(np.fromfile(filepath, dtype=np.uint8), cv2.IMREAD_COLOR)
            if img is not None:
                images.append(img)
    return images

def load_images(paths):
    """加载图片"""
    images = []
    for path in paths:
        if os.path.isdir(path):
            images.extend(load_images_from_folder(path))
        elif os.path.isfile(path):
            img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)
            if img is not None:
                images.append(img)
        else:
            print(f"Path '{path}' is neither a valid file nor a folder.")
    return images

def preprocess_images(images):
    """对图片进行预处理"""
    preprocessed_images = []
    for img in images:
        # 转换成灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 增强对比度
        enhanced = cv2.equalizeHist(gray)
        # 转换回 BGR 色彩空间
        enhanced_bgr = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)
        preprocessed_images.append(enhanced_bgr)
    return preprocessed_images

if __name__ == "__main__":
    # 读取图片集或者文件夹（假设图片文件和文件夹的路径已经排列好）
    paths = [r"C:/Users/Administrator/Desktop/image_map_达摩洞一层"]

    images = load_images(paths)

    # 检查是否成功加载所有图像
    if len(images) == 0:
        print("Error loading images.")
    else:
        # 对图片进行预处理
        preprocessed_images = preprocess_images(images)

        # 调用拼接函数
        result = stitch_images(preprocessed_images)

        if result is not None:
            # 显示结果
            cv2.imshow("Stitched Image", result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # 保存结果
            output_path = os.path.join(os.getcwd(), f"{formatted_time}.jpg")
            cv2.imencode('.jpg', result)[1].tofile(output_path)
