class Data:
    def __init__(self, day_month_year):

        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []

        for i in day_month_year.split():
            if i != '-': date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Все хорошо'
                else:
                    return f'Неверный год'
            else:
                return f'Неверный месяц'
        else:
            return f'Неверный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('2 - 2 - 2022')
print(today)
print(Data.valid(19, 11, 2021))
print(today.valid(18, 15, 2011))
print(Data.extract('08 - 12 - 2014'))
print(today.extract('11 - 11 - 2020'))
print(Data.valid(1, 10, 2000))
