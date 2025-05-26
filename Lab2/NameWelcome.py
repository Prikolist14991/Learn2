#!/usr/bin/python3
import sys

def Welcome():
        for line in sys.stdin:
            name = line.sptrip()
            if not name:
                return
            if not name.isalpha():
                print(f"Error: Name '{name}' have wrong symbols!", file='error.txt')
            if not name[0].isupper():
                print(f"Error: Name '{name}' needs to start in uppercase!", file='error.txt')
            print(f"Nice to see you {name}!")

Welcome()




