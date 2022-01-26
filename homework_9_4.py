class Car:
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.speed = 0

    def go(self, speed=35):
        self.speed = speed
        print(f'Автомобиль {self.name} цвета {self.color} движется со скоростью {self.speed} км/ч.')

    def stop(self):
        self.speed = 0
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        if direction == 'налево' or direction == 'направо':
            print(f'Автомобиль {self.name} повернул {direction}.')
        else:
            print('Можно повернуть либо налево, либо направо')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч.')


class TownCar(Car):

    def show_speed(self):
        if self.speed >= 61:
            print(
                f'Скорость автомобиля составляет {self.speed} км/ч, что превышает допустимую скорость на {self.speed - 60} км/ч.')
        else:
            print(f'Скорость автомобиля {self.speed} км/ч.')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed >= 41:
            print(
                f'Скорость автомобиля составляет {self.speed} км/ч, что превышает допустимую скорость на {self.speed - 40} км/ч.')
        else:
            print(f'Скорость автомобиля {self.speed} км/ч.')


class PoliceCar(Car):
    is_police = True


auto_1 = PoliceCar('синий', 'Ford')
auto_1.go(20)
auto_2 = SportCar('красный', 'Ferrari')
auto_2.go(300)
auto_2.show_speed()
auto_2.turn("направо")
auto_3 = WorkCar('зеленый', 'MAN')
auto_3.go(48)
auto_3.show_speed()
auto_3.turn("налево")
auto_3.stop()
auto_3.show_speed()
auto_4 = TownCar('черный', 'Lincoln')
auto_4.go(76)
auto_4.show_speed()
auto_4.turn("налево")
