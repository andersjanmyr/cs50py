import re
import sys

def input(s):
    print(s, end='', flush=True)
    for line in sys.stdin:
        return line.strip()

def length(s):
    return len(s) >= 2 and len(s) <= 6

def letters_number_etc(s):
    # Starts with two letters
    # Only letters and numbers
    # Numbers at end
    # No leading in number zero
    match = re.match(r'^[A-Z]{2}[A-Z]*([0-9]*)$', s)
    return match and match[1][0] != '0'


def is_valid(plate):
    return length(plate) and letters_number_etc(plate)

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



main()
