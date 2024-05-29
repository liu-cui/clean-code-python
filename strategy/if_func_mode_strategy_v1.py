import json
import xml.etree.ElementTree as ET

class DataProcessor:
    def __init__(self, data_type):
        self.data_type = data_type
    
    def _json_process(self, data):
        # 假设data是一个JSON字符串
        try:
            parsed_data = json.loads(data)
            print("Processing JSON data")
            # JSON 处理逻辑
            return parsed_data
        except json.JSONDecodeError:
            print("Invalid JSON data")
            return None
    
    def _xml_process(self, data):
        # 假设data是一个XML字符串
        try:
            root = ET.fromstring(data)
            print("Processing XML data")
            # XML 处理逻辑
            return root
        except ET.ParseError:
            print("Invalid XML data")
            return None
    
    def process(self, data):
        try:
            # 动态获取并调用处理方法
            process_method = getattr(self, f'_{self.data_type}_process')
            return process_method(data)
        except AttributeError:
            print(f"No method to process data of type: {self.data_type}")
            return None

# 示例用法
# 处理 JSON 数据
json_data = '{"name": "Alice", "age": 30}'
processor = DataProcessor(data_type='json')
processed_json = processor.process(json_data)
print(processed_json)  # 输出：{'name': 'Alice', 'age': 30}

# 处理 XML 数据
xml_data = '<person><name>Alice</name><age>30</age></person>'
processor = DataProcessor(data_type='xml')
processed_xml = processor.process(xml_data)
print(processed_xml)  # 输出：<Element 'person' at 0x...>
