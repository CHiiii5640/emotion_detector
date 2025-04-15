import os
import sounddevice as sd
import soundfile as sf

# 設定參數
duration = 3  # 錄音秒數
fs = 16000  # 採樣率
DATA_DIR = "data"

# 情緒選單
emotion_map = {
    "1": "happy",
    "2": "sad",
    "3": "angry"
}

# 讓使用者選擇情緒
print("請選擇情緒：")
print("1 ➜ happy 😄")
print("2 ➜ sad 😢")
print("3 ➜ angry 😠")

emotion_input = input("請輸入對應的數字 (1/2/3)：").strip()
emotion = emotion_map.get(emotion_input)

if emotion is None:
    print("❌ 無效的輸入，請輸入 1、2 或 3")
    exit()

# 建立資料夾
emotion_dir = os.path.join(DATA_DIR, emotion)
os.makedirs(emotion_dir, exist_ok=True)

# 自動命名檔案
existing_files = os.listdir(emotion_dir)
file_number = len([f for f in existing_files if f.endswith(".wav")]) + 1
filename = os.path.join(emotion_dir, f"{file_number}.wav")

# 開始錄音
print("🎙️ 開始錄音中，請說話...")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
sf.write(filename, recording, fs)
print(f"✅ 錄音完成，已儲存為：{filename}")