# Q1

import pandas as pd
import numpy as np

df = pd.read_excel("l2.xlsx", sheet_name="Purchase data")

X = df.iloc[:, 1:4].values
y = df.iloc[:, 4].values

print("Feature Matrix (X):")
print(X)

print("\nOutput Vector (y):")
print(y)

print("\nDimensionality of Vector Space:", X.shape[1])
print("Number of Vectors:", X.shape[0])

rank = np.linalg.matrix_rank(X)
print("Rank of Feature Matrix:", rank)

pseudo_inverse = np.linalg.pinv(X)
cost = pseudo_inverse @ y

print("\nCost of Each Product:")
print("Candies:", cost[0])
print("Mangoes:", cost[1])
print("Milk Packets:", cost[2])