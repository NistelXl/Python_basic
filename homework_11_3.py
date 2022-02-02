class Lists:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(my_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Выход'
                else:
                    return f'Выход'


my_except = Lists(1)
print(my_except.my_input())
