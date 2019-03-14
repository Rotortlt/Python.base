# Задача-1:
#
# Создать класс треугольник и реализовать в нем конструктор, методы для вычисления (не печати, нужен return) площади, периметра  и вывод значений сторон треугольника на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то написать, что такой треугольник нельзя создать и сделать exit(1)

class Triangle():

    def __init__(self, side_A: int, side_B: int, side_C: int):

        self.side_A = side_A
        self.side_B = side_B
        self.side_C = side_C

        if self.side_A <= 0 or self.side_B <= 0 or self.side_A <= 0 or (self.side_A + self.side_B) <= self.side_C or (self.side_C + self.side_B) <= self.side_A  or (self.side_A + self.side_C) <= self.side_B:
            print("This triangle do not exist")
            exit()

    def perimeter(self):

        return self.side_A + self.side_B + self.side_C

    def area(self):

        self.half_per = (self.side_A + self.side_B + self.side_C) / 2

        return ((self.half_per) * (self.half_per - self.side_A) * (self.half_per - self.side_B) * (self.half_per - self.side_C)) ** 0.5



triangle1 = Triangle(5, 3, 3)

print(triangle1.perimeter())

print(triangle1.area())