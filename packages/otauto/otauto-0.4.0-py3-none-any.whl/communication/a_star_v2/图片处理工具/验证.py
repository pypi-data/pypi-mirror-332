# 使用示例
import numpy as np
from PIL import Image

from communication.a_star_v2.method.image_traits import ImageTraits
ls=[]

if __name__ == "__main__":
    # node_point_list = []
    # for i in range(1,23):
        image1 = Image.open(rf'D:\pc_work\pc_script\resource\tld_images\遇敌节点\024.png')
        image2 = Image.open(r'D:\pc_work\pc_script\resource\images_info\map_image\tld_color_2.png')
        image1_array = np.array(image1)
        image2_array = np.array(image2)

        # 裁剪 image1_array 和 image2_array，例如裁剪区域 (x, y, width, height)
        x1, y1, x2, y2 = 1258, 75, 1415, 225  # image1的裁剪区域

        # 计算原始裁剪区域的中心点
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        # 缩小比例
        scale_factor = 1

        # 新的宽度和高度
        new_width = (x2 - x1) * scale_factor
        new_height = (y2 - y1) * scale_factor

        # 计算新的裁剪区域坐标，使其居中
        new_x1 = int(center_x - new_width / 2)
        new_y1 = int(center_y - new_height / 2)
        new_x2 = int(center_x + new_width / 2)
        new_y2 = int(center_y + new_height / 2)
        image1_cropped = image1_array[new_y1:new_y2, new_x1:new_x2] # 裁剪

        x2, y2, w2, h2 = 15, 17, 122, 101  # image2的裁剪区域
        image2_cropped = image2_array[y2:y2 + h2, x2:x2 + w2]  # 裁剪

        matcher = ImageTraits()  # 只使用 SIFT
        res=matcher.draw_matches(image1_cropped, image2_array,True)  # 绘制匹配结果
        print(f"{res}")
        # node_point_list.append(res["role_position"])

# print(node_point_list)


"""



"""

# if __name__ == "__main__":
#         image1 = Image.open(f'resource/image_b/tld/001.png')
#         image2 = Image.open('resource/image_b/tld_crop/001_crop_0.png')
#         image1_array = np.array(image1)
#         image2_array = np.array(image2)
#
#         # 裁剪 image1_array 和 image2_array，例如裁剪区域 (x, y, width, height)
#         x1, y1, x2, y2 = 686, 464, 1106, 746  # image1的裁剪区域
#
#         # 计算原始裁剪区域的中心点
#         center_x = (x1 + x2) / 2
#         center_y = (y1 + y2) / 2
#
#         # 缩小比例
#         scale_factor = 0.3
#
#         # 新的宽度和高度
#         new_width = (x2 - x1) * scale_factor
#         new_height = (y2 - y1) * scale_factor
#
#         # 计算新的裁剪区域坐标，使其居中
#         new_x1 = int(center_x - new_width / 2)
#         new_y1 = int(center_y - new_height / 2)
#         new_x2 = int(center_x + new_width / 2)
#         new_y2 = int(center_y + new_height / 2)
#         image1_cropped = image1_array[new_y1:new_y2, new_x1:new_x2] # 裁剪
#
#         x2, y2, w2, h2 = 15, 17, 122, 101  # image2的裁剪区域
#         image2_cropped = image2_array[y2:y2 + h2, x2:x2 + w2]  # 裁剪
#
#         matcher = ImageMatcher()  # 只使用 SIFT
#         res=matcher.draw_matches(image1_cropped, image2_array,True)  # 绘制匹配结果
#         print(f"{res}")