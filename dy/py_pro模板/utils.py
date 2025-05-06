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