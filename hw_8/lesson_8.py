import time
import math


# №1

class Auto:

    def __init__(self, brand: str, age: int, mark: str,
                 color: str = 'unknown', weight: int = None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1

    def get_information(self):
        information = str(
            f'Brand: {self.brand}\nAge: {self.age}\n'
            f'Mark: {self.mark}\nColor: {self.color}\n'
            f'Weight: {self.weight}\n'
        )
        return information

    def add_other_date(self, color: str, weight: int):
        self.color = color
        self.weight = weight

    def show_information(self):
        print(self.get_information())


automobile_1 = Auto('sss', 22, 's1')
automobile_1.move()
automobile_1.stop()
print(automobile_1.get_information())
automobile_1.birthday()
automobile_1.add_other_date('red', 2000)
print(automobile_1.get_information())


# №2

class Truck(Auto):

    def __init__(self, brand, age, mark, max_load: int):
        super().__init__(brand, age, mark, color='Unknown', weight=None)
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)

    def get_information(self):
        information = str(
            f'\n{super().get_information()}'
            f'Max load {self.max_load}\n'
        )
        return information


class Car(Auto):

    def __init__(self, brand, age, mark, max_speed: int):
        super().__init__(brand, age, mark, color='Unknown', weight=None)
        self.max_seed = max_speed

    def move(self):
        super().move()
        print(f'max speed is {self.max_seed}')

    def get_information(self):
        information = str(
            f'\n{super().get_information()}'
            f'Max speed {self.max_seed}\n'
        )
        return information


truck_1 = Truck('ddd', 3, 'd1', 2000)
truck_2 = Truck('aaa', 2, 'a1', 2500)
truck_1.move()
truck_1.load()
truck_1.add_other_date('green', 20000)
truck_1.get_information()
truck_1.show_information()
truck_2.show_information()

car_1 = Car('www', 1, 'w1', 180)
car_1.add_other_date('black', 500)
car_1.show_information()
car_1.birthday()
car_1.show_information()
car_2 = Car('eee', 1, 'w1', 180)
car_2.show_information()


# №3

class Point:

    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'{self.__class__} with (x={self.y}, y={self.x})'

    def __str__(self):
        return f'{self.__class__.__name__} with (x={self.x}, y={self.y})'

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __del__(self):
        print("remote instance: " + str(self))


class Circle(Point):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return super().__eq__(other) and self.radius == other.radius

    def __repr__(self):
        return (
            f'{self.__class__}: with (x={self.y}, y={self.x}).'
            f' Radius of the circle = {self.radius}'
        )

    def __str__(self):
        return str(
            f'{self.__class__.__name__} with (x={self.y}, y={self.x}).'
            f' Radius of the circle = {self.radius}'
        )

    def area(self):
        print(f'{self.radius ** 2 * math.pi}')

    def edge_distance_from_origin(self):
        return super().distance_from_origin() - self.radius

    def circiumference(self):
        print(f'{self.radius * 2 * math.pi}')

    def radius_subtraction(self, other):
        result = self.radius - other.radius
        if result == 0:
            return self.create_point()

        return self.__abs__(result)

    def __abs__(self, result):
        return abs(result)

    def __sub__(self, other):
        return self.x - other.x

    def create_point(self, ):
        point_x = Point(self.x, self.y)
        return point_x

    def __del__(self):
        print("remote instance: " + str(self))


circle_1 = Circle(4, 5, 1)
circle_2 = Circle(4, 5, 1)
print(circle_2)
print(circle_2.__repr__())
result_1 = circle_1.radius_subtraction(circle_2)
circle_1.area()
print(result_1)

circle_3 = Circle(4, 5, 1)
circle_4 = Circle(4, 5, 6)
circle_4.area()
print(circle_3)
print(circle_3.__repr__())
print(circle_4.__repr__())
result_2 = circle_3.radius_subtraction(circle_4)
print(result_2)

point_1 = Point(4, 5)
point_2 = Point(5.5, -4.4)
point_3 = Point(4, 5)
print(point_1.distance_from_origin())
print(point_2.distance_from_origin())
print(point_1 == point_2)
print(point_1 == point_3)
