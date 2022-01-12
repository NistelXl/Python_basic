def gen(value1, value2):
    n = len(value1) - len(value2)
    if n > 0:
        for _ in range(n):
            value2.append(None)
    for tutor, klass in zip(value1, value2):
        yield (tutor, klass)


TUTORS = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
KLASSES = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

generator = gen(TUTORS, KLASSES)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
