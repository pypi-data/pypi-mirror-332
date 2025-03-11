import cv2
import os
from datetime import datetime
import numpy as np

# 获取当前时间
current_time = datetime.now()

# 格式化时间
formatted_time = current_time.strftime('%Y-%m-%d %H%M%S')

def stitch_images(images):
    """拼接图片"""
    stitcher = cv2.Stitcher_create()
    status, stitched_image = stitcher.stitch(images)

    if status != cv2.Stitcher_OK:
        print("Error stitching images, status code:", status)
        return None
    return stitched_image

def load_frames_from_video(video_path, frame_interval=5, crop_coords=None):
    """从视频中加载帧并根据坐标裁剪"""
    frames = []
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return frames

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:  # 每隔指定帧提取
            if crop_coords is not None:
                x1, y1, x2, y2 = crop_coords
                frame = frame[y1:y2, x1:x2]  # 裁剪图像
            frames.append(frame)
        frame_count += 1

    cap.release()
    return frames

def adjust_contrast_brightness(image, contrast=1.3, brightness=30):
    """调整图像对比度和亮度"""
    adjusted = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
    return adjusted

def preprocess_images(images):
    """对图片进行预处理"""
    preprocessed_images = []
    for img in images:
        enhanced_img = adjust_contrast_brightness(img)
        preprocessed_images.append(enhanced_img)
    return preprocessed_images

if __name__ == "__main__":
    # 视频文件路径
    video_path = r"/resource/video/Video_20250307210850.wmv"  # 替换为你的实际视频文件路径

    # 设置裁剪坐标 (x1, y1, x2, y2)
    crop_coords = (1258, 75, 1414, 207)  # 示例坐标，根据需要修改

    # 从视频中加载帧
    frames = load_frames_from_video(video_path, frame_interval=10)

    # 检查是否成功加载所有帧
    if len(frames) == 0:
        print("Error loading frames from video.")
    else:
        # 对帧进行预处理
        preprocessed_frames = preprocess_images(frames)

        # 调用拼接函数
        result = stitch_images(preprocessed_frames)

        if result is not None:
            # 显示结果
            # cv2.imshow("Stitched Image", result)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            # 保存结果
            output_path = os.path.join(os.getcwd(), f"{formatted_time}.png")
            cv2.imencode('.png', result)[1].tofile(output_path)
            print(f"Stitched image saved to {output_path}.")