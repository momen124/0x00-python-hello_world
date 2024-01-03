#!/usr/bin/python3
import random

i = random.randint(-10000, 10000)
last = abs(i) % 10
sign = -1 if i < 0 else 1  # Determine the sign

if last > 5:
    print(f"Last digit of {i} is {sign * last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {i} is {sign * last} and is 0")
else:
    print(f"Last digit of {i} is {sign * last} and is less than 6 and not 0")
