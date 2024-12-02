import os
os.environ["KERAS_BACKEND"] = "torch"

import moonshine  # 或者 moonshine_onnx
try:
    result = moonshine.transcribe('D:/test/1234.mp3', 'moonshine/tiny')
    print(result)
except Exception as e:
    print(f"Error: {e}")

