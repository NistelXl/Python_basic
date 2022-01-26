class Stationery:
    def __init__(self, title='Handtool'):
        self.title = title

    def draw(self):
        print(f'Start drawing. {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title} pen.')


class Pencil(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title} pencil.')


class Handle(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title} handle.')


stat = Stationery()
stat.draw()
pen = Pen('Bic')
pen.draw()
pencil = Pencil('Kohinoor')
pencil.draw()
handle = Handle('Kolben')
handle.draw()
