# 🎧 Emotion Detector

這是一個簡單的情緒語音偵測器，支援使用麥克風錄音，並透過 eGeMAPS 聲學特徵 + 機器學習模型來判斷使用者的情緒狀態。

---

## 📁 專案結構
emotion_detector/
├── data/                        # 儲存訓練語音資料（happy/sad/angry/…）
├── recorded.wav                 # 即時錄音檔案
├── egemaps_features.csv        # 特徵擷取後的資料
├── emotion_model.joblib        # 訓練好的情緒分類模型
├── train_emotion_classifier.py # 訓練模型
├── recognize_emotion.py        # 語音情緒偵測
├── extract_egemaps_features.py # 擷取 eGeMAPS 特徵
└── .gitignore
---

## 🔧 使用流程

1. 錄音並自行分類至 `data/` 資料夾下（如：`happy/`、`sad/`、`angry/`）
2. 執行 `extract_egemaps_features.py` 擷取語音特徵
3. 執行 `train_emotion_classifier.py` 訓練模型
4. 執行 `recognize_emotion.py` 即時偵測使用者語音情緒
5. Unity 可透過 `current_emotion.json` 讀取偵測結果（可用於控制動畫、變色等）

---

## 📦 依賴套件

```bash
pip install sounddevice soundfile opensmile scikit-learn joblib pandas