res = []

with open('nginx_logs.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        el = [line[:line.index('-') - 1]]
        line = line[line.index('"') + 1:]
        el.append(line[:line.index(' ')])
        el.append(line[line.index('/'):line.index('H') - 1])
        res.append(tuple(el))

print('[')
for element in res:
    print(el, end=',\n')
print(']')