# Q3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

df = pd.read_excel("l2.xlsx", sheet_name="IRCTC Stock Price")

price = df["Price"].dropna()

print("Mean using NumPy:", np.mean(price))
print("Variance using NumPy:", np.var(price))


def my_mean(arr):
    return sum(arr) / len(arr)


def my_variance(arr):
    m = my_mean(arr)
    return sum((x - m) ** 2 for x in arr) / len(arr)


print("Mean using Function:", my_mean(price))
print("Variance using Function:", my_variance(price))

runs = 10

start = time.perf_counter()
for _ in range(runs):
    np.mean(price)
np_mean_time = (time.perf_counter() - start) / runs

start = time.perf_counter()
for _ in range(runs):
    my_mean(price)
my_mean_time = (time.perf_counter() - start) / runs

start = time.perf_counter()
for _ in range(runs):
    np.var(price)
np_var_time = (time.perf_counter() - start) / runs

start = time.perf_counter()
for _ in range(runs):
    my_variance(price)
my_var_time = (time.perf_counter() - start) / runs

print("\nAverage Execution Time")
print("NumPy Mean:", np_mean_time)
print("Custom Mean:", my_mean_time)
print("NumPy Variance:", np_var_time)
print("Custom Variance:", my_var_time)

wed = df[df["Day"] == "Wed"]
print("\nWednesday Mean:", wed["Price"].mean())

apr = df[df["Month"] == "Apr"]
print("April Mean:", apr["Price"].mean())

loss_prob = len(df[df["Chg%"] < 0]) / len(df)
print("\nProbability of Loss:", loss_prob)

wed_profit = len(wed[wed["Chg%"] > 0]) / len(wed)
print("Probability of Profit on Wednesday:", wed_profit)

cond_prob = len(wed[wed["Chg%"] > 0]) / len(wed)
print("Conditional Probability of Profit Given Wednesday:", cond_prob)

plt.scatter(df["Day"], df["Chg%"])
plt.xlabel("Day")
plt.ylabel("Chg %")
plt.title("Change % vs Day")
plt.show()