import random
import os
import shutil

# Initialize counters and lists
count = 0
numbers = []    # List to store generated random numbers
evens = []      # List to store even numbers
odds = []       # List to store odd numbers

# Generate 100 random integers between 1 and 100,000
while count < 100:
    num = random.randint(1, 100000)
    count += 1
    numbers.append(num)

# Separate numbers into evens and odds
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

# Check if the folder "numbers" exists
# If it exists, delete it and recreate to ensure it's clean
# Otherwise, just create the folder
if os.path.exists("numbers"):
    shutil.rmtree("numbers")
os.mkdir("numbers")

# Define path for the odds file and write all odd numbers line by line
path_odds = os.path.join("numbers", "odds.txt")
with open(path_odds, "w") as file_odds:
    for n in odds:
        file_odds.write(str(n) + "\n")

# Define path for the evens file and write all even numbers line by line
path_evens = os.path.join("numbers", "evens.txt")
with open(path_evens, "w") as file_evens:
    for n in evens:
        file_evens.write(str(n) + "\n")
