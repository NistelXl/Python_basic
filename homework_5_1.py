def odd_nums(n):
    for i in range(1, n+1, 2):
        yield i


odd_to_5 = odd_nums(7)
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))