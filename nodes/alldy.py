from .baidu_image_crawler import BaiduImageCrawler
import comfy.utils
import importlib
import sys
import random

import subprocess
import json
class DynamicPyNode:

    def _call_external_script(self, script_path, params):
        try:
            # 根据文件后缀选择解释器
            if script_path.endswith('.py'):
                cmd = ["python", script_path, json.dumps(params)]
            elif script_path.endswith('.js'):
                cmd = ["node", script_path, json.dumps(params)]
            elif script_path.endswith('.exe'):
                cmd = [script_path, json.dumps(params)]
            else:
                return ""
                
            process = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            return process.stdout
        except subprocess.CalledProcessError as e:
            print(f"脚本执行失败：{e.stderr}")
            return ""
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                 "nametype": (["路径", "json值"],),
                "script_path": ("STRING", {"default": "H:\docker\share\custom_nodes\Comfyui-chenx\dy\py_pro1\main.py","multiline": True}),
                "input_params": ("STRING", {"multiline": True}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute_script"
    CATEGORY = "Chenx/Dynamic"

    def execute_script(self, nametype,script_path, input_params,seed):
        random.seed(seed)
        if nametype == "json值":
            script_path = "H:\docker\share\custom_nodes\Comfyui-chenx\dy\py_pro2\main.py"
        else:
            pass
            # 调用外部Python脚本的核心逻辑
        result = self._call_external_script(script_path, input_params)
        return (result,)