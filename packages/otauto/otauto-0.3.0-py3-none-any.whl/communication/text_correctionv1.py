from fuzzywuzzy import process
from loguru import logger
"""
功能:通过模糊匹配来纠正的词
日期:2025-2-13 16:48:54
描述:
    ocr识别错误纠正
"""
# 正确词列表
# correct_words = ["雇佣剑客"]

def correct_term(input_word, correct_words,threshold=70):
    """
    纠正输入词
    :param input_word: 输入的词
    :param correct_words: 正确的词列表
    :param threshold: 相似度阈值
    """
    try:
        # 使用模糊匹配找到最相似的词
        result = process.extractOne(input_word, correct_words)
        # logger.success(f"输入: {input_word} → 纠正后: {result[0]} similarity: {result[1]}")
        # 若相似度超过阈值则返回纠正后的词，否则返回原词
        return result[0] if result[1] > threshold else None
    except Exception as e:
        logger.error(f"纠正词时发生错误: {e}")

# 示例
# input_word = "佣剑"
# corrected = correct_term(input_word)
# print(f"输入: {input_word} → 纠正后: {corrected}")
