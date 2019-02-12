# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class ToyFactory:

    def __init__(self, name, color, type_toy):
        self.name = name
        self.color = color
        self.type_toy = type_toy

    def _purchase_raw_materials(self):
        print('-- Закупка сырья...')

    def _tailoring(self):
        print('-- пошив...')

    def _coloring(self):
        print('-- окраска...')

    def start_production(self):
        input('Запуск производства, нажмите пробел:')
        self._purchase_raw_materials()
        self._tailoring()
        self._coloring()

toy = ToyFactory('Мишка', 'белый', 'животное')
toy.start_production()
print('Наименование игрушки - {}, цвет {}, тип - {}'.format(toy.name, toy.color, toy.type_toy))

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy:

    def __init__(self, name, color):
        self.name = name
        self.color = color

class ToyAnimal(Toy):

    def __init__(self, name, color):
        Toy.__init__(self, name, color)
        self.type_toy = 'животное'

class ToyMult(Toy):

    def __init__(self, name, color):
        Toy.__init__(self, name, color)
        self.type_toy = 'персонаж мультфильма'

class ToyFactory:

    def start_production(self, name, color, type_toy):
        input('Запуск производства, нажмите пробел:')
        self._purchase_raw_materials()
        self._tailoring()
        self._coloring()
        if type_toy == 'животное':
            return ToyAnimal(name, color)
        elif type_toy == 'персонаж мультфильма':
            return ToyMult(name, color)

    def _purchase_raw_materials(self):
        print('-- Закупка сырья...')

    def _tailoring(self):
        print('-- пошив...')

    def _coloring(self):
        print('-- окраска...')

factory = ToyFactory()
toy2 = factory.start_production('Гуффи', 'серый', 'персонаж мультфильма')
print('Наименование игрушки - {}, цвет {}, тип - {}'.format(toy2.name, toy2.color, toy2.type_toy))

