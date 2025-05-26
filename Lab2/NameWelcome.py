#!/usr/bin/python3
import sys

def Welcome():
        for line in sys.stdin:
            name = line.strip()
            Last(name)
        if sys.stdin == None:
            a = input("Say your name")
            Last(a)
def Last(name):
    error = open("error.txt", 'a')
    if not name:
        return
    if not name[0].isupper():
        error.write(f"Error: Name '{name}' needs to start in uppercase!")
    if not name.isalpha():
        error.write(f"Error: Name '{name}' have wrong symbols!")
    else:
        print(f"Hello! {name}")



Welcome()





