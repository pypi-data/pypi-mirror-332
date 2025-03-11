import json
import atexit


class Recorder:
    def __init__(self):
        self.data = {}

    def put(self, key, value):
        self.data[key] = value

    def save_to_file(self):
        try:
            with open('record.json', 'w', encoding='utf-8') as f:
                json_str = json.dumps(self.data, indent=2)
                f.write(json_str)
        except Exception as e:
            print(f"Error saving to file: {e}")


# 创建一个全局的 Recorder 实例
recorder = Recorder()

# 注册退出时的回调函数，确保数据在记录完毕之后再保存
atexit.register(recorder.save_to_file)
