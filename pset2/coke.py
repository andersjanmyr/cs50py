import sys

def read_input():
    print('Insert coin: ', end='', flush=True)
    for line in sys.stdin:
        try:
            n = int(line)
        except:
            return 0
        if n in [5, 10, 25]:
            return n
        else:
            return 0


def read_until_fully_paid(amount):
    due = amount
    while due > 0:
        print('Amount due:', due)
        n = read_input()
        due -= n
    return -due

def main():
    change = read_until_fully_paid(50)
    print('Change Owed:', change)


main()
