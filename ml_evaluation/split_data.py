import csv
import random

input_file = "ml_evaluation/data/Data.csv"   # your file
train_file = "ml_evaluation/data/train.csv"
test_file = "ml_evaluation/data/test.csv"

# Read data
with open("Data.csv", "r", encoding="utf-8") as f:
    reader = list(csv.reader(f))

header = reader[0]
data = reader[1:]

# Shuffle data
random.shuffle(data)

# Split 80-20
split_index = int(0.8 * len(data))
train_data = data[:split_index]
test_data = data[split_index:]

# Write train file
with open("train_file", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(train_data)

# Write test file
with open("test_file", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(test_data)

print("Done! Files created:")
print("Train:", train_file)
print("Test:", test_file)
