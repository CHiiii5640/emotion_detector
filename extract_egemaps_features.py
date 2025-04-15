import os
import pandas as pd
import opensmile

DATA_ROOT = "data"
smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals,
)

features_list = []

for emotion in os.listdir(DATA_ROOT):
    emotion_path = os.path.join(DATA_ROOT, emotion)
    if os.path.isdir(emotion_path):
        for file in os.listdir(emotion_path):
            if file.endswith(".wav"):
                path = os.path.join(emotion_path, file)
                feats = smile.process_file(path)
                feats["filename"] = path
                feats["emotion"] = emotion
                features_list.append(feats)

df = pd.concat(features_list)
df.to_csv("egemaps_features.csv", index=False)
print("✅ 已儲存特徵與標籤至 egemaps_features.csv")