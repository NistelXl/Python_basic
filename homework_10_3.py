class Cell:
    __count: int

    def __init__(self, count: int):
        assert count > 0, 'Количество ячеек должно быть больше ноля'
        self.__count = count

    def __add__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count + other.count
        return Cell(value)

    def __sub__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count - other.count
        assert value > 0, 'Разность ячеек меньше ноля'
        return Cell(value)

    def __mul__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count * other.count
        return Cell(value)

    def __truediv__(self, other: 'Cell'):
        self.validate_item(other)
        value = round(self.count / other.count)
        return Cell(value)

    def __str__(self):
        return str(self.__count)

    def validate_item(self, other):
        assert isinstance(other, self.__class__)

    @property
    def count(self) -> int:
        return self.__count

    @staticmethod
    def order(cell_object: 'Cell', count_per_row: int) -> str:
        items = '*' * cell_object.count
        chunks = [items[idx:idx + count_per_row] for idx in range(0, len(items), count_per_row)]

        return '\n'.join(chunks)


first = Cell(8)
second = Cell(7)
big = Cell(20)

print(first + second)
print(first - second)
print(first * second)
print(first / second)

print(Cell.order(big, 5))
