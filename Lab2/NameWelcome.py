#!/usr/bin/python3
import sys

def Welcome():
        for line in sys.stdin:
            error = open("error.txt", 'a')
            name = line.strip()
            if not name:
                return
            if not name.isalpha():
                error.write(f"Error: Name '{name}' have wrong symbols!")
            if not name[0].isupper():
                error.write(f"Error: Name '{name}' needs to start in uppercase!")
            else:
                print(f"Hello! {name}")


Welcome()





