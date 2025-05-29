#!/usr/bin/python3
import random
import sys

def Stdintest():
    try:
        A = float(input())
        B = random.randint(-10,10)
        stder = A/B
    except ValueError as e:
        print('Wrong value')
    except ZeroDivisionError as e:
        print('B = 0')
    else:
        print(stder)

Stdintest()
