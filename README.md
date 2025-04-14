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
├── record_save.py              # 錄音並儲存為資料集
├── current_emotion.json        # Unity 讀取的結果（偵測情緒）
└── .gitignore
---

## 🔧 使用流程

1. 執行 `record_save.py` 錄製語音並自行分類到 `data/happy/`, `data/sad/`, `data/angry/` 等資料夾
2. 執行 `extract_egemaps_features.py` 擷取語音特徵（輸出 `egemaps_features.csv`）
3. 執行 `train_emotion_classifier.py` 訓練情緒模型（產出 `emotion_model.joblib`）
4. 執行 `recognize_emotion.py` 透過麥克風即時偵測情緒，並儲存為 `current_emotion.json`
5. 在 Unity 內讀取 `current_emotion.json`，控制畫面顏色、動畫或角色行為

---

## 🧠 支援的情緒

目前模型支援分類以下情緒（視你的語音資料分類而定）：

- happy
- sad
- angry

---

## 📦 安裝依賴套件

```bash
pip install sounddevice soundfile opensmile scikit-learn joblib pandas