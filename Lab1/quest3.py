#!/usr/bin/python3
import math
import sys

def Last():
    try:
        inp = float(input)
        if inp == 0:
            raise Exception()
    except Exception:
        print("inp == 0")
    except EOFError:
        print("Error")
    else:
        sqrt_num = math.sqrt(inp)
        with open('output.txt', 'w') as f:
            f.write(f"{inp} ")
