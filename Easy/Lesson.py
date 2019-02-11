# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'поехала'

    def stop(self):
        return 'остановилась'

    def turn(self, direction):
        return 'повернула ' + direction

class SportCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'поехала'

    def stop(self):
        return 'остановилась'

    def turn(self, direction):
        return 'повернула ' + direction

class WorkCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'поехала'

    def stop(self):
        return 'остановилась'

    def turn(self, direction):
        return 'повернула ' + direction

class PoliceCar:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'поехала'

    def stop(self):
        return 'остановилась'

    def turn(self, direction):
        return 'повернула ' + direction

town_car = TownCar('100', 'Серебристый', 'Honda Fit')
print('{} {}'.format(town_car.name, town_car.go()))
print(town_car.is_police)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'поехала'

    def stop(self):
        return 'остановилась'

    def turn(self, direction):
        return 'повернула ' + direction

class TownCar(Car):
    pass

class SportCar(Car):
    pass

class WorkCar(Car):
    pass

class PoliceCar(Car):

    def __init__(Car, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

police_car = PoliceCar('120', 'темный', 'FORD ')
print('{} {}'.format(police_car.name, police_car.turn('на лево')))
print(police_car.is_police)