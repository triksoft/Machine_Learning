# Q4

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_excel("l2.xlsx", sheet_name="thyroid0387_UCI")

print("Data Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nNumeric Summary:")
print(df.describe())

print("\nMean:")
print(df.select_dtypes(include=np.number).mean())

print("\nVariance:")
print(df.select_dtypes(include=np.number).var())

print("\nOutliers (IQR Method):")
for col in df.select_dtypes(include=np.number).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]
    print(col, len(outliers))

encoded_df = df.copy()

for col in encoded_df.select_dtypes(include="object").columns:
    if encoded_df[col].nunique() <= 10:
        encoded_df = pd.get_dummies(encoded_df, columns=[col])
    else:
        le = LabelEncoder()
        encoded_df[col] = le.fit_transform(encoded_df[col].astype(str))

print("\nEncoded Data:")
print(encoded_df.head())