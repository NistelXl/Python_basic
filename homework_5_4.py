src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([i for j, i in enumerate(src) if j != 0 and i > src[j - 1]])