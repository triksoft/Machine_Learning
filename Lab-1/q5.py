import random
import statistics

numbers = []

for i in range(100):
    random_number = random.randint(100, 150)
    numbers.append(random_number)

print("Generated Numbers:")
print(numbers)

mean_value = statistics.mean(numbers)
median_value = statistics.median(numbers)
mode_value = statistics.mode(numbers)

print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)