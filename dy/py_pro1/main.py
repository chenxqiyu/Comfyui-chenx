#!/usr/bin/env python3
import sys
import json
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# 导入文件操作工具函数
import json

def file_operation(filename, key=None, value=None):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    
    if value is not None:
        data[key] = value
        with open(filename, 'w') as f:
            json.dump(data, f)
    
    return data.get(key) if key else data


# 人名数组
NAMES = ["张三", "李四", "王五", "赵六", "钱七"]

def runway():
    try:
        # 解析输入参数（兼容直接传参和stdin两种方式）
        if len(sys.argv) > 1:
            params = json.loads(sys.argv[1])
        else:
            params = json.loads(sys.stdin.read())

        
        #switch params
        if "prompt" in params:
            params = params["prompt"]
        elif "text" in params:
            params = params["text"]
        else:
            pass

        # 示例处理逻辑
        # 获取当前人名索引
        name_index = file_operation('data.json', 'name_index')
        name_index = int(name_index) if name_index else 0
        
        # 循环输出人名
        current_name = NAMES[name_index % len(NAMES)]
        file_operation('data.json', 'name_index', name_index + 1)
        
        result = {
            "ddd": params,
            "processed": {
                "timestamp": time.time(),
                "input_length": len(str(params)),
                "current_name": current_name,
                "name_index": name_index
            }
        }


        
        # 使用通用函数处理计数器
        counter = file_operation('data.json', 'counter')
        counter = int(counter) + 1 if counter else 1
        file_operation('data.json', 'counter', counter)
        result["counter"] = counter
        
        # 返回标准JSON格式
        print(json.dumps(result, indent=2, ensure_ascii=False))

    except Exception as e:
        # 错误时返回结构化错误信息
        error_msg = {
            "error": str(e),
            "type": type(e).__name__,
            "params": sys.argv[1] if len(sys.argv) > 1 else None
        }
        print(json.dumps(error_msg, ensure_ascii=False))
        sys.exit(1)

if __name__ == "__main__":
    runway()