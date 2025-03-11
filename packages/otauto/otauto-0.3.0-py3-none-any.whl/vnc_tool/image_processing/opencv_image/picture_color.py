import cv2
import numpy as np
from sklearn.neighbors import KDTree
"""
更新日志:2024-11-5 20:15:06
查找图片中的所有颜色
1. 修改了get_unique_colors函数，使其在去除相似颜色时，使用KD树来加速查询过程。
2. 修改了get_unique_colors函数的参数，增加了distance_threshold参数，用于指定相似颜色的距离阈值。
3. 修改了get_unique_colors函数的返回值，返回一个包含所有唯一颜色的列表，而不是一个字典。
4. 修改了get_unique_colors函数的代码，使其在去除相似颜色时，只保留距离最小的颜色。

"""
def rgb_to_hex(rgb):
    """
    将RGB颜色转换为十六进制颜色代码
    :param rgb:
    :return:
    """
    return '{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def color_distance(color1, color2):
    """
    计算两个颜色之间的欧氏距离
    :param color1:
    :param color2:
    :return:
    """
    return np.sqrt(np.sum((np.array(color1) - np.array(color2)) ** 2))

def get_unique_colors(image_path, distance_threshold=10):
    """
    获取图片中的所有颜色，并去除相似颜色
    示例使用
    image_path = 'Snipaste_2024-11-05_20-02-51.png'  # 替换成你图片的路径
    colors = get_unique_colors(image_path, distance_threshold=10)  # 距离阈值可以根据需求调整
    print(colors)
    :param image_path: 图片路径
    :param distance_threshold: 相似颜色的距离阈值
    :return:
    """
    # 读取图片
    img = cv2.imread(image_path)
    # 将BGR格式转换为RGB格式
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 获取图片的所有像素颜色
    pixels = img.reshape((-1, 3))
    # 转换为元组并去重
    unique_colors = set(tuple(color) for color in pixels)
    # 将颜色排序
    sorted_unique_colors = sorted(unique_colors)
    # 去除相似颜色
    reduced_colors = []
    for color in sorted_unique_colors:
        if not reduced_colors:
            reduced_colors.append(color)
        else:
            if all(color_distance(color, existing_color) >= distance_threshold for existing_color in reduced_colors):
                reduced_colors.append(color)
    # 转换为十六进制表示
    hex_colors = [rgb_to_hex(color) for color in reduced_colors]
    return hex_colors


def get_unique_colors_tree(image_path, distance_threshold=10):
    """
    获取图片中的所有颜色，并去除相似颜色,此方法获取颜色更多,效率高
    示例使用
    image_path = 'Snipaste_2024-11-05_20-02-51.png'  # 替换成你图片的路径
    colors = get_unique_colors_tree(image_path, distance_threshold=10)  # 距离阈值可以根据需求调整
    print(colors)
    :param image_path: 图片路径
    :param distance_threshold: 相似颜色的距离阈值
    :return:
    """
    # 读取图片
    img = cv2.imread(image_path)
    # 将BGR格式转换为RGB格式
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 获取图片的所有像素颜色
    pixels = img.reshape((-1, 3))
    # 转换为元组并去重
    unique_colors = list(set(map(tuple, pixels)))
    # 构造KD树
    tree = KDTree(unique_colors)
    # 标记已访问的颜色
    visited = set()
    reduced_colors = []
    for i, color in enumerate(unique_colors):
        if i in visited:
            continue
        reduced_colors.append(color)
        # 获取在distance_threshold范围内的所有颜色
        distances, indices = tree.query_radius([color], r=distance_threshold, return_distance=True)
        for idx in indices[0]:
            visited.add(idx)
    # 转换为十六进制表示
    hex_colors = [rgb_to_hex(color) for color in reduced_colors]
    return hex_colors


# 示例使用
image_path = r'D:\pc_work\dtwsv2_v4.0\res\dtws\image_map_达摩洞一层\demo_1.png'  # 替换成你图片的路径
colors = get_unique_colors(image_path, distance_threshold=10)  # 距离阈值可以根据需求调整
print(colors)