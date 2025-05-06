from .nodes.alldy import DynamicPyNode
from .nodes.key_value_node import KeyValueNode

NODE_CLASS_MAPPINGS = {
    "DynamicPyNode": DynamicPyNode,
    "KeyValueNode": KeyValueNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DynamicPyNode": "动态Python",
    "KeyValueNode": "json键值对"
}