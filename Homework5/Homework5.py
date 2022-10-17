# Задание 5.
# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

from re import A
from turtle import pen


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"{self.title}"


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"{self.title} Запуск отрисовки ручкой"


class Pensil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"{self.title} Запуск отрисовки карандашом"


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"{self.title} Запуск отрисовки маркером"


a = Pen("Ручка: ")
b = Pensil("Карандаш: ")
c = Handle("Маркер: ")
print(a.draw())
print(b.draw())
print(c.draw())
