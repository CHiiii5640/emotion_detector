import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# 載入特徵資料
df = pd.read_csv("egemaps_features.csv")

# 只選擇數值型欄位當作特徵
X = df.select_dtypes(include=['number']).drop(columns=["label"], errors="ignore")
y = df["emotion"]

# 分割資料集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 訓練模型
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 評估模型
y_pred = model.predict(X_test)
print("📊 分類結果：")
print(classification_report(y_test, y_pred))

# ✅ 儲存模型 + 欄位名稱（為推論使用）
joblib.dump((model, list(X.columns)), "emotion_model_with_columns.joblib")
print("✅ 模型與欄位已儲存為 emotion_model_with_columns.joblib")