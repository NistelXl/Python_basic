# Задание 1

translate = {'zero' : 'ноль', 'one' : 'один', 'two' : 'два', 'three' : 'три', 'four' : 'четыре', 'five' : 'пять', 'six' : 'шесть', 'seven' : 'семь', 'eight' : 'восемь', 'nine' : 'девять', 'ten' : 'десять'}
def num_translate():
    key = input("Введите число от 0 до 10 на английском языке: ")
    print(f"Ваше число на русском языке:  {translate.get(key)}")


num_translate()


