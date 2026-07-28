# Q7

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_excel("l2.xlsx", sheet_name="thyroid0387_UCI")

temp = df.copy()

for col in temp.columns:
    temp[col] = temp[col].astype(str)
    temp[col] = LabelEncoder().fit_transform(temp[col])

binary_cols = [col for col in temp.columns if temp[col].nunique() == 2]

data = temp.iloc[:20]

n = len(data)

jc = np.zeros((n, n))
smc = np.zeros((n, n))
cos = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        v1 = data.iloc[i]
        v2 = data.iloc[j]

        f11 = f10 = f01 = f00 = 0

        for col in binary_cols:
            a = v1[col]
            b = v2[col]

            if a == 1 and b == 1:
                f11 += 1
            elif a == 1 and b == 0:
                f10 += 1
            elif a == 0 and b == 1:
                f01 += 1
            else:
                f00 += 1

        den = f11 + f10 + f01

        jc[i][j] = f11 / den if den != 0 else 0
        smc[i][j] = (f11 + f00) / (f11 + f10 + f01 + f00)
        cos[i][j] = cosine_similarity(
            v1.values.reshape(1, -1),
            v2.values.reshape(1, -1)
        )[0][0]

plt.figure(figsize=(6,5))
sns.heatmap(jc, annot=True)
plt.title("Jaccard Coefficient")
plt.show()

plt.figure(figsize=(6,5))
sns.heatmap(smc, annot=True)
plt.title("Simple Matching Coefficient")
plt.show()

plt.figure(figsize=(6,5))
sns.heatmap(cos, annot=True)
plt.title("Cosine Similarity")
plt.show()