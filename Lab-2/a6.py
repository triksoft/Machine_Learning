# Q6

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_excel("l2.xlsx", sheet_name="thyroid0387_UCI")

temp = df.copy()

for col in temp.columns:
    temp[col] = temp[col].astype(str)
    temp[col] = LabelEncoder().fit_transform(temp[col])

v1 = temp.iloc[0].values.reshape(1, -1)
v2 = temp.iloc[1].values.reshape(1, -1)

cos = cosine_similarity(v1, v2)

print("Cosine Similarity:", cos[0][0])