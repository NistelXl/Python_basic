# Задание 1

# Не делал ввод значений через input, т.к. в задании это не требуется

duration = 400153

day = (duration) // (24 * 3600)
hour = (duration - 24 * day * 3600) // 3600
min = (duration - 24 * day * 3600 - 3600 * hour) // 60
sec = duration % 60
if day == 0 and hour == 0 and min == 0:
    print(sec,"сек")
elif day == 0 and hour == 0:
    print(min, "мин", sec, "сек")
elif day == 0:
    print(hour,"час",min,"мин",sec,"сек")
else:
    print(day, "дн", hour, "час", min, "мин", sec, "сек")

# Вариант с циклом для нескольких значений

duration = [53,153,4153,400153]
for n in duration:
    day = n // (24 * 3600)
    hour = (n - 24 * day * 3600) // 3600
    min = (n - 24 * day * 3600 - 3600 * hour) // 60
    sec = n % 60
    if day == 0 and hour == 0 and min == 0:
        print(sec,"сек")
    elif day == 0 and hour == 0:
        print(min, "мин", sec, "сек")
    elif day == 0:
        print(hour,"час",min,"мин",sec,"сек")
    else:
        print(day, "дн", hour, "час", min, "мин", sec, "сек")

