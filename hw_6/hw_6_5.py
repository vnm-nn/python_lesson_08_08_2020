# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
# атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
# “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать
# экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Launch draw {self.title}'

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'You took {self.title}. Launch pen draw'

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'You took {self.title}. Launch pencil draw'

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'You took {self.title}. Launch handle draw'

pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())