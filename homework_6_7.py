import sys

LEN = 12 + 2
need_row = int(sys.argv[1])
new_value = sys.argv[2]

with open('bakery.csv', 'r+', encoding='utf-8') as f:
    f.seek((need_row - 1) * LEN)
    f.write(f'{new_value:>12}\n')