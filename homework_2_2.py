# Задание 2

my_list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list_2 = []

for i in my_list_1:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            my_list_2.append(f'"{int(i):02}"')
        else:
            my_list_2.append(f'"{i[0]}{int(i[1:]):02}"')
    else:
        my_list_2.append(i)

print(" ".join(my_list_2))
