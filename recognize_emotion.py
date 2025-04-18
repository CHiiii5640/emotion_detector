import sounddevice as sd
import soundfile as sf
import opensmile
import joblib
import pandas as pd
import json
import time

# 初始化
print("🌀 情緒偵測器持續運行中")
duration = 3
fs = 16000
output_wav = "recorded.wav"

# 載入模型
model, expected_columns = joblib.load("emotion_model_with_columns.joblib")

# 初始化 opensmile
smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals,
)

# 持續執行
try:
    while True:
        print("\n🎙️ 錄音中...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
        sf.write(output_wav, recording, fs)
        print("✅ 錄音完成，儲存為", output_wav)

        print("🔍 擷取聲音特徵...")
        features = smile.process_file(output_wav)
        features.columns = features.columns.astype(str)

        # 欄位對齊
        for col in expected_columns:
            if col not in features.columns:
                features[col] = 0.0
        features = features[expected_columns]

        # 預測
        prediction = model.predict(features)[0]
        proba = model.predict_proba(features).max()
        print(f"💡 偵測到的情緒為：{prediction}（信心度: {proba:.2f}）")

        # 寫入 JSON 給 Unity
        output = {
            "emotion": prediction,
            "confidence": round(float(proba), 4),
        }
        with open("current_emotion.json", "w") as f:
            json.dump(output, f)
        print("📝 已寫入 current_emotion.json")

        time.sleep(5)  # 每 5 秒執行一次，可自行調整間隔

except KeyboardInterrupt:
    print("🛑 已停止情緒偵測。")