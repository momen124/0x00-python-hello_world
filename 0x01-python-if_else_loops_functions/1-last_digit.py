#!/usr/bin/python3
import random

i = random.randint(-10000, 10000)
last = abs(i) % 10

if i < 0:
    last = -last

if last > 5:
    print(f"Last digit of {i} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {i} is {last} and is 0")
else:
    print(f"Last digit of {i} is {last} and is less than 6 and not 0")
