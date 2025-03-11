import cv2
import os
from datetime import datetime

"""
更新日志:2024-11-5 08:04:08
功能:图片拼接
注意图片之间要有重复的部分,不然会拼接失败

"""

# 获取当前时间
current_time = datetime.now()

# 格式化时间
formatted_time = current_time.strftime('%Y-%m-%d%H%M%S')

def stitch_images(images):
    # 创建一个Stitcher对象
    stitcher = cv2.Stitcher_create()

    # 拼接图像
    status, stitched_image = stitcher.stitch(images)

    if status != cv2.Stitcher_OK:
        print("Error stitching images, status code:", status)
        return None
    return stitched_image


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images


def load_images(paths):
    images = []
    for path in paths:
        if os.path.isdir(path):
            images.extend(load_images_from_folder(path))
        elif os.path.isfile(path):
            img = cv2.imread(path)
            if img is not None:
                images.append(img)
        else:
            print(f"Path '{path}' is neither a valid file nor a folder.")
    return images


if __name__ == "__main__":
    # 读取图片集或者文件夹（假设图片文件和文件夹的路径已经排列好）
    paths = [
        r"C:\Users\Administrator\Desktop\image_map"
    ]

    images = load_images(paths)

    # 检查是否成功加载所有图像
    if len(images) == 0:
        print("Error loading images.")
    else:
        # 调用拼接函数
        result = stitch_images(images)

        if result is not None:
            # 显示结果
            cv2.imshow("Stitched Image", result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # 保存结果
            cv2.imwrite(f"{formatted_time}.jpg", result)

