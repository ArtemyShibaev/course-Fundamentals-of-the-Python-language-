# task 1
import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        print(self.__color[0])
        time.sleep(7)
        print(self.__color[1])
        time.sleep(2)
        print(self.__color[2])
        time.sleep(5)


traffic = TrafficLight()
traffic.running()


# task2

class Road:

    def __init__(self, length, width):
        self.l = length
        self.w = width

    def count(self):
        count = self.l * self.w * 25 * 0.05
        print(count)


r = Road(20, 5000)
r.count()


# task3

class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 15000, 'bonus': 5000}


class Position(Worker):
    def get_full_name(self):
        print(f"Full name is {self.name} {self.surname}")

    def get_total_income(self, income, bonus):
        print(f'Total income is {income + bonus}')


p = Position('John', 'Johnson', 'CEO', 20000)

p.get_full_name()
p.get_total_income(20000, 5000)


# task4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('the car went')

    def stop(self):
        print('the car stopped')

    def turn(self, right):
        if right == 1:
            print('the car turned right')
        else:
            print('the car turned left')

    def show_speed(self):
        print('Your speed is ', self.speed)

    def car_info(self):
        print('This is a car')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('speed exceeded!!!')
        else:
            print('The speed is correct')

    def car_info(self):
        print('This is a TownCar')


class SportCar(Car):
    def car_info(self):
        print('This is a SportCar')


class WorkCar(Car):

    def car_info(self):
        print('This is a WorkCar')

    def show_speed(self):
        if self.speed > 40:
            print('speed exceeded!!!')
        else:
            print('The speed is correct')


class PoliceCar(Car):
    def car_info(self):
        print('This is a PoliceCar')


tc = TownCar(60, 'Gray', 'Bus', False)
tc.car_info()
print(TownCar)
tc.go()
tc.turn(0)
tc.show_speed()

sc = SportCar(0, 'Yellow', 'car', False)
sc.car_info()
sc.stop()
sc.show_speed()

wc = WorkCar(50, 'Black', 'Truck', False)
wc.car_info()
wc.go()
wc.turn(1)
wc.show_speed()

pc = PoliceCar(0, 'White', 'car', True)
pc.car_info()
pc.stop()
pc.show_speed()


# task5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('start drawing')


class Pen(Stationery):

    def draw(self):
        print('you draw with a pen')


class Pencil(Stationery):

    def draw(self):
        print('you draw with a pencil')


class Handle(Stationery):

    def draw(self):
        print('you draw with a handle')


st = Stationery('Stationery')
print(st.title)
st.draw()

pencil = Pencil('Pencil')
print(pencil.title)
pencil.draw()

pen = Pen('Pen')
print(pen.title)
pen.draw()

handle = Handle('Handle')
print(handle.title)
handle.draw()