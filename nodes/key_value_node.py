import comfy.utils
import json
import random

class KeyValueNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": "", "multiline": False}),
                "content": ("STRING", {"multiline": True,"forceInput": True}),
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})

            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_value"
    CATEGORY = "Chenx/KeyValue"

    def get_value(self, key, content, seed):
        try:
            random.seed(seed)
            data = json.loads(content)
            
            # 如果包含点号，按照路径查找
            if '.' in key:
                keys = key.split('.')
                result = data
                for k in keys:
                    if isinstance(result, dict) and k in result:
                        result = result[k]
                    else:
                        return (f"找不到键: {key}，请检查路径是否正确",)
                return (str(result),)
            
            # 直接在顶层查找
            if key in data:
                return (str(data[key]),)
            
            # 递归搜索嵌套结构中的键
            found_value = self.search_key(data, key)
            if found_value is not None:
                return (str(found_value),)
                
            return (f"找不到键: {key}，如果是嵌套值，请使用点号表示法，例如: 'processed.input_length'",)
        except Exception as e:
            return (f"错误: {str(e)}",)
    
    def search_key(self, data, target_key):
        """递归搜索JSON中的键"""
        if isinstance(data, dict):
            # 直接在当前字典中查找
            if target_key in data:
                return data[target_key]
            
            # 递归搜索所有嵌套字典
            for key, value in data.items():
                result = self.search_key(value, target_key)
                if result is not None:
                    return result
        
        # 如果是列表，搜索列表中的每个元素
        elif isinstance(data, list):
            for item in data:
                result = self.search_key(item, target_key)
                if result is not None:
                    return result
        
        # 未找到
        return None
        