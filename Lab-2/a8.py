# Q8

import pandas as pd
import numpy as np

df = pd.read_excel("l2.xlsx", sheet_name="thyroid0387_UCI")

for col in df.columns:

    numeric = pd.to_numeric(df[col], errors="coerce")

    if numeric.notna().sum() > 0:

        Q1 = numeric.quantile(0.25)
        Q3 = numeric.quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        has_outlier = ((numeric < lower) | (numeric > upper)).any()

        if has_outlier:
            df[col] = numeric.fillna(numeric.median())
        else:
            df[col] = numeric.fillna(numeric.mean())

    else:

        mode = df[col].mode()

        if not mode.empty:
            df[col] = df[col].fillna(mode[0])

print(df.isnull().sum())
print(df.head())