pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install useful-moonshine@git+https://github.com/usefulsensors/moonshine.git
pip install streamlit
运行 streamlit run web.py即可打开网页版，上传音频文件，并转化

音频文件要求：
检查音频格式: 确保音频文件是单声道 (mono) 和正确的采样率（通常是 16kHz 或 16,000 Hz）。可以使用工具如 librosa 或 ffmpeg 转换音频：
ffmpeg -i 456.wav -ar 16000 -ac 1 output.wav
替换 456.wav 为你的文件路径，生成的新文件可以尝试重新输入
