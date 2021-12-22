# Задание 3

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(my_list)):

    if my_list[i].replace("+","").replace("-","").isdigit():
        if len(my_list[i]) == 1:
            my_list[i] = f'"0{my_list[i]}"'
        elif (my_list[i][0] == '+' or my_list[i][0] == '-') and len(my_list[i]) == 2:
            my_list[i] = '"{}"'.format(my_list[i][0] + '0' + my_list[i][1:])
        elif len(my_list[i]) == 2:
            my_list[i] = f'"{my_list[i]}"'

print(" ".join(my_list))
