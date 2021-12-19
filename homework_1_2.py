# Задание 2

# Вариант 1
cube_list = []

for i in range(1,1001):
    if i % 2 != 0:
        cube_list.append(i ** 3)

all_sum = 0
for n in cube_list:
    n_sum = 0
    temp = n
    while (temp != 0):

        n_sum += temp % 10
        temp = temp // 10

    if n_sum % 7 == 0:
        all_sum += n



print(all_sum)

# Вариант 2

cube_list = []

for i in range(1,1001):
    if i % 2 != 0:
        cube_list.append(i ** 3 + 17)
        # добавили 17 к каждому элементу списка, создав новый список

all_sum = 0
for n in cube_list:
    n_sum = 0
    temp = n
    while (temp != 0):

        n_sum += temp % 10
        temp = temp // 10

    if n_sum % 7 == 0:
        all_sum += n


print(all_sum)

# Вариант 3

cube_list = []

for i in range(1,1001):
    if i % 2 != 0:
        cube_list.append(i ** 3)

all_sum = 0
for n in cube_list:
    n += 17  # добавили 17 к каждому элементу списка, не создавая новый список
    n_sum = 0
    temp = n
    while (temp != 0):

        n_sum += temp % 10
        temp = temp // 10

    if n_sum % 7 == 0:
        all_sum += n



print(all_sum)