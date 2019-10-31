# -*- coding: UTF-8 -*-


"""
pass
"""

from classtools import AttrDisplay
import random
import decorators


class Character(AttrDisplay):
    """
    A class that defines the general character.

    :method remove_health: Modifies in place health and is_alive parameters
    :method deal_damage: Calculates and returns the value of damage
    """

    def __init__(self, name):
        """
        Character class constructor.
        :param name: Character name
        :type name: string
        """
        self.name = name
        self.agility = self.agility()
        self.constitution = self.constitution()
        self.health = self.calculate_health()

    @staticmethod
    def agility():
        """
        :return: default 50
        """
        return 50

    @staticmethod
    def constitution():
        """
        :return: default 50
        """
        return 50

    def calculate_health(self):
        """
        Calculate characters health
        :return: self.health
        """
        return self.constitution * 2

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
        print(f'{self.name} loses {damage_received} health points.')
        if self.health < 1:
            self.health = 0
            print(f'{self.name} is killed.')

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
        Character.__init__(self, name)

    @decorators.general_mod(10)
    def constitution(self):
        return Character.constitution()

    @decorators.general_mod(2)
    def deal_damage(self):
        return Character.deal_damage(self)


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
        Character.__init__(self, name)

    @decorators.general_mod(-10)
    def agility(self):
        return Character.agility()

    @decorators.reduce_damage(-2)
    def remove_health(self, other):
        return Character.remove_health(self, other)


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
        Character.__init__(self, name)

    @decorators.general_mod(10)
    def agility(self):
        return Character.agility()

    @decorators.dodge(10)
    def remove_health(self, other):
        return Character.remove_health(self, other)

