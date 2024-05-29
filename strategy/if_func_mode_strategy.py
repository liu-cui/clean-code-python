"""
利用函数封装

将相似逻辑封装成函数或方法，减少重复的条件判断，提高代码复用性
"""


def clean_text(data):
    print("clean text")
    return data

def validate_numeric(data):
    print("validate numeric")
    return data


# def process_data(data_type, data):
#     if data_type == "text":
#         return clean_text(data)
#     elif data_type  == "numeric":
#         return validate_numeric(data)
#     # ...其他类型处理


# 改进后
class DataProcessor:
    def __init__(self, data_type):
        self.data_type = data_type

    def process(self, data):
        return getattr(self, f"_{self.data_type}_process")(data)
    
    def _text_process(self, data):
        return clean_text(data)
    
    def _numeric_process(self, data):
        return validate_numeric(data)
    # ...其他类型处理方法

processor = DataProcessor("numeric")
processor.process(data="wang")
