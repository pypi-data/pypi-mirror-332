import cv2
import os
from datetime import datetime
import numpy as np

# 获取当前时间
current_time = datetime.now()

# 格式化时间
formatted_time = current_time.strftime('%Y-%m-%d %H%M%S')


def stitch_images_horizontal(images):
    """水平拼接图片"""
    stitcher = cv2.Stitcher_create()
    status, stitched_image = stitcher.stitch(images)
    if status != cv2.Stitcher_OK:
        print("Error stitching images horizontally, status code:", status)
        return None
    return stitched_image


def stitch_images_vertical(images):
    """垂直拼接图片"""
    stitcher = cv2.Stitcher_create(mode=cv2.Stitcher_PANORAMA)
    status, stitched_image = stitcher.stitch(images)
    if status != cv2.Stitcher_OK:
        print("Error stitching images vertically, status code:", status)
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


def adjust_contrast_brightness(image, contrast=1.3, brightness=30):
    """调整图像对比度和亮度"""
    adjusted = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
    return adjusted


def preprocess_images(images):
    """对图片进行预处理"""
    preprocessed_images = []
    for img in images:
        # 调整对比度和亮度
        enhanced_img = adjust_contrast_brightness(img)
        preprocessed_images.append(enhanced_img)
    return preprocessed_images


if __name__ == "__main__":
    # 读取图片集或者文件夹（假设图片文件和文件夹的路径已经排列好）
    paths = [r"C:/Users/Administrator/Desktop/image_全商盟货船"]

    images = load_images(paths)

    # 检查是否成功加载所有图像
    if len(images) == 0:
        print("Error loading images.")
    else:
        # 对图片进行预处理
        preprocessed_images = preprocess_images(images)

        # 用户选择拼接方向
        direction = input("Enter 'h' for horizontal stitching or 'v' for vertical stitching: ").strip().lower()

        if direction == 'h':
            result = stitch_images_horizontal(preprocessed_images)
        elif direction == 'v':
            result = stitch_images_vertical(preprocessed_images)
        else:
            print("Invalid direction input. Please enter 'h' or 'v'.")
            result = None

        if result is not None:
            # 显示结果
            cv2.imshow("Stitched Image", result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # 保存结果
            output_path = os.path.join(os.getcwd(), f"{formatted_time}.jpg")
            cv2.imencode('.jpg', result)[1].tofile(output_path)