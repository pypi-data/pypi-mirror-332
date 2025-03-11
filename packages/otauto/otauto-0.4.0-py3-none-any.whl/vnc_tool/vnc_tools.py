import time

from loguru import logger

"""
功能:vnc服务器键鼠操作
日期:2025-2-13 18:47:46
描述:
    键鼠操作
"""

class VncTools:
    """
    VncTools工具类,用于VNC服务器键鼠操作
    """
    def __init__(self, vnc):
        self.vnc = vnc


    def text_input(self,text,delay_time=0.1):
        """
        文本输入,只支持字母和数字输入
        :param text: 文本内容
        :param delay_time: 延迟时间
        :return:
        """
        result_list=list(text) # 将字符串转换为列表
        for text in result_list:
            self.key_press_op(text,delay_time)

    def is_correct_and_compare(self,s):
        """
        判断字符串是否为两个数字通过斜杠 / 分隔的形式，并比较两个数字的值。
        两边必须是数字。
        # 测试
            test_string1 = '1317/1317'
            result1 = is_correct_and_compare(test_string1)
            print(f"'{test_string1}' 格式正确且符合比较条件: {result1}")

            test_string2 = '1317/2634'
            result2 = is_correct_and_compare(test_string2)
            print(f"'{test_string2}' 格式正确且符合比较条件: {result2}")

            test_string3 = 'abc/123'
            result3 = is_correct_and_compare(test_string3)
            print(f"'{test_string3}' 格式正确且符合比较条件: {result3}")

            test_string4 = '123/'
            result4 = is_correct_and_compare(test_string4)
            print(f"'{test_string4}' 格式正确且符合比较条件: {result4}")
        :param s: 需要判断的字符串
        :return: 如果格式正确且符合条件返回 True，格式不正确或条件不满足返回 False
        """
        # 定义正则模式：确保斜杠两边都是数字
        pattern = r'^\d+/\d+$'

        # 检查格式是否正确
        if not re.match(pattern, s):
            return False

        # 分割字符串
        parts = s.split('/')

        # 转换为整数
        num1 = int(parts[0])
        num2 = int(parts[1])

        # 比较数值
        return num1 < num2 / 2

    def is_point_in_rectangle(self,point, rect):
        """
        判断点是否在矩形内
        :param point:   (x, y) 坐标
        :param rect:     (x_min, y_min, x_max, y_max) 矩形坐标
        :return:   True or False
        """
        x, y = point
        x_min, y_min, x_max, y_max = rect
        return x_min <= x <= x_max and y_min <= y <= y_max

    def is_in_eliminate_scope(self, midpoint: tuple, eliminate_scope: list) -> bool:
        """
        判断给定点是否在消除的矩形范围内
        :param midpoint: 中心点坐标 (x, y)
        :param eliminate_scope: 需要消除的矩形范围列表
        :return: 如果在消除范围内，返回True，否则返回False
        """
        return any(self.is_point_in_rectangle(midpoint, rect) for rect in eliminate_scope)


    def contains_all_elements(self,list1, list2,list_num):
        """判断list1是否是list2的子集"""
        if len(list1)>=list_num:
            set1 = set(list1)
            set2 = set(list2)
            return set2.issubset(set1)

    def get_merge_dicts(self,dict_a, dict_b):
        """合并两个字典，如果有相同的键，则以 dict_a 的值为准"""
        merged_dict = {}
        # 先处理 dict_a
        for key in dict_a:
            if key not in merged_dict:
                merged_dict[key] = {}
            merged_dict[key].update(dict_a[key])
        # 再处理 dict_b
        for key in dict_b:
            if key not in merged_dict:
                merged_dict[key] = {}
            # 更新 dict_b 的键，如果存在相同的键，则以 dict_a 的值为准
            for subkey, value in dict_b[key].items():
                if subkey not in merged_dict[key]:  # 只有当子键不存在时才添加
                    merged_dict[key][subkey] = value
        return merged_dict

    def find_Shortcut_bar_function(self):
        """
        找到快捷栏字典中每个键对应的图片,用于快捷栏功能查找
        #示例代码:
            res=find_Shortcut_bar_function(shortcut_bar_dict, dic_image_hand)
            print(res)
        :return: '1': 'res/dtws/role_skill/穿云剑.bmp', '2': 'res/dtws/role_skill/如封似闭.bmp', }
        """
        # 创建一个空的新字典
        new_dict = {}
        if self.dic_image_hand:
            # 对于快捷栏字典中的每个键和值
            for key, value in shortcut_bar_dict.items():
                # 遍历图像字典来查找匹配的坐标
                for image_path, coords in self.dic_image_hand.items():
                    # 遍历图像字典中的坐标列表
                    for coord in coords:
                        # 如果坐标的两点坐标(x, y)落在快捷栏的区域内
                        if value[0] <= coord[0] <= value[2] and value[1] <= coord[1] <= value[3]:
                            # 将快捷键与图像路径的映射加入新字典
                            new_dict[key] = image_path

        return new_dict

    def find_yolo(self, category_name, con: float = 0.8, eliminate_scope: list = None, model_name: str = "model") -> bool:
        """
        根据类别名和置信度进行查找，查找是否有符合条件的物体
        :param category_name: 类别名，可以是字符串或字符串列表
        :param con: 置信度阈值
        :param eliminate_scope: 需要消除的矩形范围（通过中心点排除）
        :param model_name: 模型名称
        :return: 如果找到符合条件的物体，返回True，否则返回False
        """
        if eliminate_scope is None:
            # 默认的消除范围
            eliminate_scope = [(1233, 258, 1422, 482), (36, 594, 347, 741)]

        #查找框架中的yolo数据
        if self.dic_yolo_ocr:#{'红色名称': [(660, 69, 0, 0)], '红名怪': [(691, 211, 0, 0), (734, 237, 0, 0)]}
            for key, value_list in self.dic_yolo_ocr.items():
                if key in category_name :
                    for value in value_list:
                        if not self.is_in_eliminate_scope(value[:2], eliminate_scope):
                            return True

        # 获取YOLO模型的检测结果
        yolo_list = self.vnc.find_yolov5(model_name)

        if not yolo_list:
            return False

        # 将 category_name 处理为列表形式，确保可以支持单个字符串或字符串列表的输入
        if isinstance(category_name, str):
            category_name = [category_name]

        # 检查每个检测项
        for yolo_item in yolo_list:
            class_name = yolo_item["class_name"]
            confidence = yolo_item["confidence"]
            midpoint = yolo_item["midpoint"]

            # 如果类别名匹配且置信度符合要求，并且不在消除范围内
            if class_name in category_name and confidence >= con and not self.is_in_eliminate_scope(midpoint, eliminate_scope):
                return True

        return False

    def find_ppocr_op(self, x1, y1, x2, y2):
        """
        在指定的矩形区域内查找PP-OCR识别到的文字
        :param x1:  矩形左上角的x坐标
        :param y1:  矩形左上角的y坐标
        :param x2:  矩形右下角的x坐标
        :param y2:  矩形右下角的y坐标
        :return:  返回识别到的文字字典
        """
        return self.vnc.find_ppocr(x1, y1, x2, y2)

    def find_ppocr_word_op(self, text: str, x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        在指定坐标区域内查找特定文本。

        :param text: 要查找的文本，可以是用 '|' 分隔的多个文本
        :param x1: 矩形区域左上角 x 坐标
        :param y1: 矩形区域左上角 y 坐标
        :param x2: 矩形区域右下角 x 坐标
        :param y2: 矩形区域右下角 y 坐标
        :return: 如果找到任意一个文本则返回 True，否则返回 False
        """
        res_dict = self.vnc.find_ppocr(x1, y1, x2, y2)
        # logger.debug(f"识别结果: {res_dict}")

        # Split the input text by '|' to handle multiple search terms
        search_terms = text.split('|')

        if res_dict:
            for key in res_dict.keys():
                for term in search_terms:
                    if term in key:  # Consider using `if term.lower() in key.lower()` for case-insensitivity

                        return True
        return False

    def find_ppocr_word_click(self, text: str, x1: int, y1: int, x2: int, y2: int,x3: int=0, y3: int=0,delay_time:float=0.1) -> bool:
        """
        在指定坐标区域内查找特定文本。

        :param text: 要查找的文本，可以是用 '|' 分隔的多个文本
        :param x1: 矩形区域左上角 x 坐标
        :param y1: 矩形区域左上角 y 坐标
        :param x2: 矩形区域右下角 x 坐标
        :param y2: 矩形区域右下角 y 坐标
        :param x3:  x坐标偏移量
        :param y3:  y坐标偏移量
        :param delay_time:   延迟时间
        :return: 如果找到任意一个文本则返回 True，否则返回 False
        """
        res_dict = self.vnc.find_ppocr(x1, y1, x2, y2)
        # logger.debug(f"识别结果: {res_dict}")

        # Split the input text by '|' to handle multiple search terms
        search_terms = text.split('|')

        if res_dict:
            for key,vlue in res_dict.items():
                for term in search_terms:
                    if term in key:  # Consider using `if term.lower() in key.lower()` for case-insensitivity
                        x,y=vlue[0][0]+x1+x3,vlue[0][1]+y1+y3
                        self.mouse_left_click_op(x,y,delay_time)
                        return True
        return False


    def get_yolo_click(self, category_name, con: float = 0.8,key_num:int=1,x3:int=0,y3:int=0,delay_time:float=0.1,eliminate_scope: list = None, model_name: str = "model") -> bool:
        """
        根据类别名和置信度进行查找，查找是否有符合条件的物体

        :param category_name: 类别名，可以是字符串或字符串列表
        :param con: 置信度阈值
        :param key_num: 鼠标左右键 1 左键 3 右键
        :param x3: 鼠标点击偏移量x
        :param y3: 鼠标点击偏移量y
        :param delay_time: 鼠标点击延迟时间
        :param eliminate_scope: 需要消除的矩形范围（通过中心点排除）
        :param model_name: 模型名称
        :return: 如果找到符合条件的物体，返回True，否则返回False
        """
        if eliminate_scope is None:
            # 默认的消除范围
            eliminate_scope = [(1233, 258, 1422, 482), (36, 594, 347, 741),(975,48,1241,181)]

        #查找框架中的yolo数据
        if self.dic_yolo_ocr:#{'红色名称': [(660, 69, 0, 0)], '红名怪': [(691, 211, 0, 0), (734, 237, 0, 0)]}
            for key, value_list in self.dic_yolo_ocr.items():
                if key in category_name :
                    for value in value_list:
                        if not self.is_in_eliminate_scope(value[:2], eliminate_scope):
                            if key_num==1:
                                self.mouse_left_click_op(value[0]+x3, value[1]+y3, delay_time=delay_time)
                            elif key_num==3:
                                self.mouse_right_click_op(value[0]+x3, value[1]+y3, delay_time=delay_time)
                            return True

        # 获取YOLO模型的检测结果
        yolo_list = self.vnc.find_yolov5(model_name)

        if not yolo_list:
            return False

        # 将 category_name 处理为列表形式，确保可以支持单个字符串或字符串列表的输入
        if isinstance(category_name, str):
            category_name = [category_name]

        # 检查每个检测项
        for yolo_item in yolo_list:
            class_name = yolo_item["class_name"]
            confidence = yolo_item["confidence"]
            midpoint = yolo_item["midpoint"]

            # 如果类别名匹配且置信度符合要求，并且不在消除范围内
            if class_name in category_name and confidence >= con and not self.is_in_eliminate_scope(midpoint, eliminate_scope):
                if key_num==1:
                    self.mouse_left_click_op(midpoint[0]+x3, midpoint[1]+y3, delay_time=delay_time)
                elif key_num==3:
                    self.mouse_right_click_op(midpoint[0]+x3, midpoint[1]+y3, delay_time=delay_time)
                return True
        return False

    def find_value_with_length(self,data_dict: dict, colors: str, len_num: int = 4) -> dict:
        """
        判断字典中是否存在某个颜色值对应的列表长度大于指定长度，配合多色查找使用
        示例:
        a_dict = {
        'ffffff': {
            1: [(1273, 128), (1273, 129), (1274, 128), (1274, 129), (1275, 128), (1275, 129), (1276, 128), (1276, 129),
                (1277, 128), (1277, 129)],
            2: [(1280, 131), (1280, 132), (1281, 131), (1281, 132)],
            13: [(1326, 149), (1326, 150)],
            28: [(1384, 226), (1384, 227), (1385, 226), (1385, 227)]
        },
        '000000': {
            1: [(1173, 128), (1173, 129), (1174, 128)],
            2: [(1180, 131), (1180, 132)],
            3: [(1190, 141), (1190, 142)]
            }
        }
        colors = "ffffff|000000"
        len_num = 4
        result = find_value_with_length(a_dict, colors, len_num)
        print(result)  # 应该打印 {'ffffff': True, '000000': False}
        :param data_dict: 颜色数据的字典
        :param colors: 颜色，支持多颜色，用"|"隔开表示
        :param len_num: 长度
        :return: 字典，表示每个颜色的查找结果
        """
        result = {}
        color_list = colors.split("|")

        if data_dict:
            for color in color_list:
                if color in data_dict:
                    result[color] = any(len(value) > len_num for value in data_dict[color].values())
                else:
                    result[color] = False
        return result

    def find_colors_vnc(self, color, x1, y1, x2, y2,  tolerance:int=10,distance_threshold=2):
        """
        局部颜色识别,可以识别多个单色
        :param color: 需要识别的颜色,多个颜色用"|"隔开
        :param x1: 截图区域左上角x坐标
        :param y1: 截图区域左上角y坐标
        :param x2: 截图区域右下角x坐标
        :param y2: 截图区域右下角y坐标
        :param tolerance: 容差
        :param distance_threshold: 距离阈值
        :return: {'f0e61f', [(346, 54)]}
        """
        return self.vnc.colors_vnc(color,x1,y1,x2,y2, tolerance,distance_threshold)









