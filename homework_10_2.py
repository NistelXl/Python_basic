from abc import ABC, abstractmethod


class Clothes(ABC):
    total = 0

    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        if isinstance(self.__size, str) or self.__size <= 0:
            raise ValueError('Значение должно быть положительным')
        return self.__size

    @abstractmethod
    def get_size(self):
        pass


class Coat(Clothes):
    def get_size(self):
        __v = self.size
        numbers = float(f'{__v / 6.5 + 0.5 :0.2f}')
        Clothes.total += numbers
        return f'{numbers} метра'


class Suit(Clothes):
    def get_size(self):
        __h = self.size
        numbers = float(f'{__h * 2 + 0.3 :0.2f}')
        Clothes.total += numbers
        return f'{numbers} метра'


coat = Coat(54)
print(coat.get_size())

suit = Suit(1.88)
print(suit.get_size())

suit_1 = Suit(0.7)
print(suit_1.get_size())

print(Clothes.total, 'метра')
