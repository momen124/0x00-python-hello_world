#!/usr/bin/python3
def pow(a, b):
    if b >= 0:
        result = 1
        for _ in range(b):
            result *= a
    else:
        result = 1.0
        for _ in range(-b):
            result /= a

    # Format the result to limit the number of digits after the decimal point
    formatted_result = "{:.15e}".format(result)

    return formatted_result
