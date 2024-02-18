import re
import sys

def remove_vowels(s):
    return re.sub(r'[AEIOUYaeiouy]', '', s)

def main():
    print('Input: ', end='', flush=True)
    for line in sys.stdin:
        print(remove_vowels(line))
        break

main()

