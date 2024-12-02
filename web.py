import os
#设置环境变量
os.environ["KERAS_BACKEND"] = "torch"
import streamlit as st
import moonshine
import time
import librosa
import soundfile as sf


# 设置页面标题
st.title("MoonShine 语音转文本系统")

# 上传音频文件
uploaded_file = st.file_uploader("上传音频文件", type=["wav", "mp3", "m4a"])

if uploaded_file is not None:
    # 确保临时文件夹存在
    temp_dir = "temp_audio"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # 保存上传的文件
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # 显示文件名
    st.write(f"上传的文件: {uploaded_file.name}")

    # 添加开始转译按钮
    if st.button("开始转译"):
        # 加载模型
        model = moonshine.load_model('moonshine/tiny')

        # 创建进度条
        progress_bar = st.progress(0)
        status_text = st.empty()

        # 读取音频文件
        audio, sr = librosa.load(file_path, sr=None)

        # 分割音频文件成小段
        chunk_duration = 10  # 每个片段的长度（秒）
        chunk_size = int(chunk_duration * sr)
        chunks = [audio[i:i + chunk_size] for i in range(0, len(audio), chunk_size)]

        # 转录音频
        transcription = ""
        for i, chunk in enumerate(chunks):
            # 更新进度条
            progress = (i + 1) / len(chunks)
            progress_bar.progress(progress)
            status_text.text(f"正在转录... ({i + 1}/{len(chunks)})")

            # 转录当前片段
            chunk_file = os.path.join(temp_dir, f"temp_chunk_{i}.wav")
            sf.write(chunk_file, chunk, sr)
            chunk_transcription = moonshine.transcribe(chunk_file, 'moonshine/tiny')

            # 确保 chunk_transcription 是字符串
            if isinstance(chunk_transcription, list):
                chunk_transcription = ' '.join(chunk_transcription)

            transcription += chunk_transcription

            # 删除临时文件
            os.remove(chunk_file)

            # 模拟处理时间
            time.sleep(0.1)

        # 显示最终转录结果
        st.success("转录完成！")
        st.write("转录结果:")
        st.write(transcription)

        # 清理临时文件
        os.remove(file_path)