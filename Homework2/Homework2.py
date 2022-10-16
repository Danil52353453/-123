# Задание 2.
# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.
# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т

class Road:
    def __init__(self, _length, _width,volume,thickness):
        self._length = _length
        self._width = _width
        self.volume = volume
        self.thickness= thickness

    def mass(self):
        return self._length * self._width * self.volume * self.thickness

class Mass(Road):
    def __init__(self, _length, _width, volume, thickness):
        super().__init__(_length, _width, volume, thickness)
a = Mass(20,5000,25,0.05)
print(a.mass(),f"кг")
