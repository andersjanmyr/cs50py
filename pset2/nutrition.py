import sys

def input(s):
    print(s, end='', flush=True)
    for line in sys.stdin:
        return line.strip()

table = {
        'apple': 130,
        'avocado': 50,
        'banana': 110,
        'cantaloupe': 50,
        'grapefruit': 60,
        'grapes': 90,
        'honeydew melon': 50,
        'kiwifruit': 90,
        'lemon': 15,
        'lime': 20,
        'nectarine': 60,
        'orange': 80,
        'peach': 60,
        'pear': 100,
        'pineapple': 50,
        'plums': 70,
        'strawberries': 50,
        'sweet cherries': 100,
        'tangerine': 50,
        'watermelon': 80,
        }

def calories(item):
    i = item.lower()
    if i in table:
        return table[i]
    return None

def main():
    item = input("Item: ")
    cal = calories(item)
    if cal != None:
        print('Calories:', cal)

main()
