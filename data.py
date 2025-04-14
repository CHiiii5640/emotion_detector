import pandas as pd
df = pd.read_csv("egemaps_features.csv")
print(df["emotion"].value_counts())