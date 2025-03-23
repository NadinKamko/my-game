from abc import ABC, abstractmethod

# создаем абстрактный класс с абстрактным методом

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# создаем конкретные классы наследующие абстрактному
class Sword(Weapon):
    def attack(self):
        return 'Боец наносит удар мечом.'

class Bow(Weapon):
    def attack(self):
        return 'Боец стреляет из лука.'

# модификация класса Fighter
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        return self.weapon.attack()

# Реализация боя, демонстрационный механизм
class Monster:
    def __init__(self, name):
        self.name = name

    def take_damage(self):
        return f'Монстр {self.name} получает урон.'

def fight(fighter: Fighter, monster: Monster):
    print(fighter.attack())
    print(monster.take_damage())
    print('Монстр побежден!\n')

# создаем бойца и монстра
fighter = Fighter(Sword())
monster = Monster('Гоблин')

#бой с мечом
fight(fighter, monster)

# меняем оружие на лук
fighter.change_weapon(Bow())

#бой с луком
fight(fighter, monster)




