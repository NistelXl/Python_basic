class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_profit(self):
        return f'{sum(self.income.values())}'


people = Position('Ivanon', 'Ivan', 'Plumber', 70000, 15000)
print(people.get_full_name())
print(people.position)
print(people.get_full_profit())
