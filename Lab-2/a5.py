# Q5

import pandas as pd

df = pd.read_excel("l2.xlsx", sheet_name="thyroid0387_UCI")

binary_cols = []

for col in df.columns:
    values = df[col].dropna().unique()
    if len(values) == 2:
        binary_cols.append(col)

temp = df[binary_cols].copy()

for col in temp.columns:
    temp[col] = pd.factorize(temp[col])[0]

v1 = temp.iloc[0]
v2 = temp.iloc[1]

f11 = f10 = f01 = f00 = 0

for a, b in zip(v1, v2):
    if a == 1 and b == 1:
        f11 += 1
    elif a == 1 and b == 0:
        f10 += 1
    elif a == 0 and b == 1:
        f01 += 1
    elif a == 0 and b == 0:
        f00 += 1

jc = f11 / (f11 + f10 + f01)
smc = (f11 + f00) / (f11 + f10 + f01 + f00)

print("Jaccard Coefficient:", jc)
print("Simple Matching Coefficient:", smc)