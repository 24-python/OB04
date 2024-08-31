class Fighter():
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon



class Monster():
    def __init__(self, name):
        self.name = name


from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
class Sword(Weapon):
    def attack(self):
        print("Игрок нанес удар мечом")

class Bow(Weapon):
    def attack(self):
        print("Игрок выстрелил из лука")

f = Fighter("ВОВАН")

f.change_weapon(Sword())
print("Игрок выбрал меч")
f.weapon.attack()
print("Монстр побежден")

f.change_weapon(Bow())
print("Игрок выбрал лук")
f.weapon.attack()
print("Монстр побежден")
