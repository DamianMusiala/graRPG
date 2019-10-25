# -*- coding: UTF-8 -*-
from classtools import AttrDisplay
import random


class Creature(AttrDisplay):

    def __init__(self, name, agility=50, constitution=50, speed=50, isAlive=True):
        self.name = name
        self.agility = agility
        self.constitution = constitution
        self.speed = speed
        self.isAlive = isAlive
        self.health = self.agility * 2

    def removeHealth(self, other):
        taking_damage = other if other >= 0 else 0
        self.health -= taking_damage
        if self.health < 1:
            self.health = 0
            self.isAlive = False
        print(f'{self.name} traci {taking_damage} punktów życia')

    def dealDamage(self):
        damage = random.randint(1, 10)
        print(f'{self.name} zadaje {damage} obrażeń')
        return damage


class Warrior(Creature):

    def __init__(self, name):
        Creature.__init__(self, name, agility=60)

    def dealDamage(self):
        return Creature.dealDamage(self) + 2  # to mi się do końca nie podoba -
        # powinna być zmienna modyfikator w klasie i podklasie


class Knight(Creature):

    def __init__(self, name):
        Creature.__init__(self, name, speed=40)

    def removeHealth(self, other):
        Creature.removeHealth(self, other - 2)  # zamienic na zmienną modyfikator


class Thief(Creature):

    def __init__(self, name):
        Creature.__init__(self, name, speed=60)

    def removeHealth(self, other):
        chance = random.randint(1, 10)
        if chance == 5:
            print(f'{self.name} robi unik')
            Creature.removeHealth(self, other=0)
        else:
            Creature.removeHealth(self, other)


class Battle:
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2

    def round(self):
        if self.obj1.speed > self.obj2.speed:
            self.obj2.removeHealth(self.obj1.dealDamage())
            self.obj1.removeHealth(self.obj2.dealDamage())
        elif self.obj2.speed > self.obj1.speed:
            self.obj1.removeHealth(self.obj2.dealDamage())
            self.obj2.removeHealth(self.obj1.dealDamage())
        else:
            self.obj2.removeHealth(self.obj1.dealDamage())  # wiem, że to nie do końca tak powinno być
            self.obj1.removeHealth(self.obj2.dealDamage())

    def fight(self):
        n = 1
        while n <= 20:
            if self.obj1.isAlive == True and self.obj2.isAlive == True:
                print(f'Runda: {n}')
                self.round()
                n += 1
            else:
                if not self.obj1.isAlive:
                    print(f'{self.obj1.name} ginie.')
                elif not self.obj2.isAlive:
                    print(f'{self.obj2.name} ginie.')
                break
        if self.obj1.health > self.obj2.health:
            print(f'Wygrywa: {self.obj1.name}')
        elif self.obj2.health > self.obj1.health:
            print(f'Wygrywa: {self.obj2.name}')
        else:
            print('REMIS!')

# zad. 5 Ekwipunek


if __name__ == '__main__':
    cre01 = Knight('Optimus')
    cre02 = Thief('Megatron')
    pojedynek = Battle(cre01, cre02)
    pojedynek.fight()
    box = [cre01, cre02]
    print('\n### Wyniki ####')
    for i in box:
        print(i)
