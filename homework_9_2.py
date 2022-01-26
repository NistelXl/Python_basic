class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def total_weight(self, weight=25, thickness=5):
        return f'Asphalt weight: {(self._length * self._width * weight * thickness) / 1000} tons'


road_1 = Road(5000, 20)
print(road_1.total_weight())
