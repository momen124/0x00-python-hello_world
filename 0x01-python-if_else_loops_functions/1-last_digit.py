#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
last = abs(n) % 10
if n < 0:
    last = -last
if last > 5:
    print(f"Last digit of {n :d} is {last :d} and is greater than 5")
elif last == 0:
    print(f"Last digit of {n :d} is {last :d} and is 0")
else:
    print(f"Last digit of {n :d} is {last :d} and is less than 6 and not 0")
