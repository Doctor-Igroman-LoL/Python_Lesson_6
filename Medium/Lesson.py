# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _defense(self, damage, armor):
        result = damage / armor
        return result

    def attack(self, attacking, target):
        target.health = target.health - (self._defense(attacking.damage, target.armor))
        target.health = int(target.health)
        return target.health

class Player(Person):
    pass

class Enemy(Person):
    pass

#---- Start_Game ----#

class Start_Game:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def commentator(self, attacking, target):
        target.health = 0 if target.health < 0 else target.health
        print('Цель по имени: {}. получил урон, в размере: {}. Текущие очки жизни составляет: '
              '{}'.format(target.name, attacking.damage, target.health))

    def alive(self, person):
       return True if person.health > 0 else False

    def winner(self, person):
        print('Победил:', person.name)

    def run(self):
        while True:
            pause = input('Нажмите Enter, чтобы продолжить этот эпичный бой ')
            if self.alive(self.hero):
                self.hero.attack(self.hero, self.enemy)
                self.commentator(self.hero, self.enemy)
                if self.alive(self.enemy):
                    pause = input('Нажмите Enter, чтобы продолжить этот эпичный бой ')
                    self.enemy.attack(self.enemy, self.hero)
                    self.commentator(self.enemy, self.hero)
                else:
                    self.winner(self.hero)
                    break
            else:
                self.winner(self.enemy)
                break


player = Player('Bug', 100, 30, 1.2)
enemy = Enemy('Virus', 75, 20, 0.9)
battle = Start_Game(player, enemy)
battle.run()


