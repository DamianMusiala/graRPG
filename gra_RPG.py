# -*- coding: UTF-8 -*-


"""
pass
"""

from classtools import AttrDisplay
from battle import Battle
import random


class Character(AttrDisplay):
    """
    A class that defines the general character.

    :method remove_health: Modifies in place health and is_alive parameters
    :method deal_damage: Calculates and returns the value of damage
    """

    def __init__(self,
                 name,
                 agility=50,
                 constitution=50):
        """
        Character class constructor.
        :param name: Character name
        :type name: string
        :param agility: It affects the order of movement
        :type agility: integer
        """
        self.name = name
        self.agility = agility
        self.constitution = constitution
        self.health = self.constitution * 2

    def is_alive(self):
        """
        :return: boolean True is health is more than 0.
        """
        return self.health > 0

    def remove_health(self, other):
        """
        Modifies in place health and is_alive parameters
        :param other: Damage dealt by opponent
        :type other: integer
        :return: None
        """
        damage_received = other if other >= 0 else 0
        self.health -= damage_received
        if self.health < 1:
            self.health = 0
        print(f'{self.name} loses {damage_received} health points.')

    def deal_damage(self):
        """
        Calculates and returns the value of damage. Draws a value from 1 to 10.
        :return: damage (integer)
        """
        damage = random.randint(1, 10)
        print(f'{self.name} deals {damage} damage.')
        return damage


class Warrior(Character):
    """
    A class that defines the warrior character.
    Warrior has +10 constitution and deals damage increased by 2
    """
    def __init__(self, name):
        """
        Warrior class constructor.
        :param name: Warrior name
        """
        Character.__init__(self, name, constitution=60)

    def deal_damage(self):
        """
        Modifies deal_damage method from parent class. Add damage_modyfikator.
        :return: damage (integer)
        """
        damage_modyfikator = 2
        damage = Character.deal_damage(self) + damage_modyfikator
        print(f'{self.name} deals {damage_modyfikator} additional damage pionts')
        return damage


class Knight(Character):
    """
    A class that defines the knight character.
    The knight takes damage reduced by 2 and has a agility reduced by 10.
    """
    def __init__(self, name):
        """
        Knight class constructor.
        :param name: Knight name.
        """
        Character.__init__(self, name, agility=40)

    def remove_health(self, other):
        """
        Modifies remove_health methon from parent class.
        Reduces damage taken by 2.
        :param other: damage taken
        :return: None
        """
        remove_health_modyfikator = 2
        Character.remove_health(self, other - remove_health_modyfikator)


class Thief(Character):
    """
    A class that defines the thief character.
    The thief has +10 agility and has a 10% chance to dodge, which negates the damage taken.
    """
    def __init__(self, name):
        """
        Thief class constructor.
        :param name: Thief name.
        """
        Character.__init__(self, name, agility=60)

    def remove_health(self, other):
        """
        The method overrides the method from the parent class.
        :param other: Damage dealt by opponent
        :return: None
        """
        chance_of_dodge = 10
        los = random.choice(range(1, 101))
        if los <= chance_of_dodge:
            print(f'{self.name} dodges.')
        else:
            Character.remove_health(self, other)


if __name__ == '__main__':
    character01 = Knight('Optimus')
    character02 = Warrior('Megatron')
    print(character01)
    print(character02)
    battle01 = Battle(character01, character02)
    battle01.fight()
    print(character01)
    print(character02)
