#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{}".format(chr(i).upper() if (122 - i) % 4 < 2 else chr(i)), end="")
