import cv2
import os
from datetime import datetime

def load_frames_from_video(video_path, frame_interval=5):
    """从视频中加载帧，返回帧的列表和总帧数"""
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
            frames.append(frame)
        frame_count += 1

    cap.release()
    return frames, frame_count

def save_frames(frames, output_folder, max_frames_per_folder=100):
    """将帧保存到指定文件夹，每个文件夹最多保存指定数量的帧"""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    folder_index = 0
    frame_index = 0
    current_folder = os.path.join(output_folder, f"frames_{folder_index}")
    os.makedirs(current_folder)

    for frame in frames:
        frame_filename = os.path.join(current_folder, f"frame_{frame_index:04d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_index += 1

        # 每达到最大帧数，则新建一个文件夹
        if frame_index >= max_frames_per_folder:
            folder_index += 1
            current_folder = os.path.join(output_folder, f"frames_{folder_index}")
            os.makedirs(current_folder)
            frame_index = 0  # 重置帧索引

if __name__ == "__main__":
    # 视频文件路径
    video_path = r"/resource/video/Video_20250308003459.wmv"  # 替换为你的实际视频文件路径
    output_folder = r"D:\pc_work\pc_script\resource\c"  # 输出文件夹路径
    max_frames_per_folder = 100  # 每个文件夹最大帧数

    # 从视频中加载帧
    frames, total_frame_count = load_frames_from_video(video_path, frame_interval=15)

    # 检查是否成功加载所有帧
    if len(frames) == 0:
        print("Error loading frames from video.")
    else:
        print(f"Total frames extracted: {len(frames)} out of {total_frame_count}.")
        # 保存帧到指定文件夹
        save_frames(frames, output_folder, max_frames_per_folder)
        print(f"Frames saved to {output_folder}.")


def crop_and_save_images(input_folder, output_folder, coordinates):
    """
    从输入文件夹中读取图片，根据给定的坐标裁剪并保存到输出文件夹中。

    :param input_folder: 输入文件夹路径，包含待裁剪的图片
    :param output_folder: 输出文件夹路径，裁剪后的图片将保存到此文件夹
    :param coordinates: 裁剪坐标，格式为 [(x1, y1, x2, y2), ...]
    """
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # 只处理图片文件
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            if image is None:
                print(f"无法读取图像: {image_path}")
                continue

            for i, (x1, y1, x2, y2) in enumerate(coordinates):
                # 检查裁剪区域是否在图像范围内
                if (x1 < 0 or y1 < 0 or x2 > image.shape[1] or y2 > image.shape[0]):
                    print(f"裁剪区域超出图像范围: {filename}, 坐标: ({x1}, {y1}, {x2}, {y2})")
                    continue

                # 裁剪图像
                cropped_image = image[y1:y2, x1:x2]

                # 构造输出文件名
                cropped_filename = f"{os.path.splitext(filename)[0]}_crop_{i}.png"
                cropped_image_path = os.path.join(output_folder, cropped_filename)

                # 保存裁剪后的图像
                success = cv2.imwrite(cropped_image_path, cropped_image)

                if success:
                    print(f"已保存裁剪图像: {cropped_image_path}")
                else:
                    print(f"未能保存裁剪图像: {cropped_image_path}")


# 使用示例
if __name__ == "__main__":
    input_folder = "resource/image_b/tld"  # 输入文件夹路径
    output_folder = "resource/image_b/tld_crop"  # 输出文件夹路径,不能有中文
    coordinates = [(686, 464, 1106, 746)]  # 示例裁剪坐标

    crop_and_save_images(input_folder, output_folder, coordinates)

