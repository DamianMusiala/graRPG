# -*- coding: UTF-8 -*-

from classtools import AttrDisplay
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
                 constitution=50,
                 is_alive=True,
                 chance_of_dodge=0,
                 remove_health_mod=0):
        """
        Character class constructor.
        :param name: Character name
        :type name: string
        :param agility: It affects the order of movement
        :type agility: integer
        :param is_alive: Indicates whether the character is alive or not
        :type is_alive: boolean
        :param remove_health_mod: Modifies damage taken
        :type remove_health_mod: integer
        """
        self.name = name
        self.agility = agility
        self.constitution = constitution
        self.is_alive = is_alive
        self.health = self.constitution * 2
        self.remove_health_mod = remove_health_mod

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
            self.is_alive = False
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
        print(f'{self.name} deals {damage_modyfikator} pionts extra-damage.')
        return Character.deal_damage(self) + damage_modyfikator


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
            Character.remove_health(self, other=0)
        else:
            Character.remove_health(self, other)


class Battle:
    """
    Battle class.
    Battle beetwen two chatacters.

    :method round: The method describing the course of the round.
    :method fight: The method describing the course of the fight.
    """
    def __init__(self, character_a, character_b):
        self.character_a = character_a
        self.character_b = character_b

    def round(self):
        """
        The method describing the course of the round.
        A character with a higher agility parameter starts the round and deals damage.
        Then the opponent deals damage.
        If the agility parameters are equal, the method randomizes the starting character.
        :return: None
        """
        if self.character_a.agility > self.character_b.agility:
            self.character_b.remove_health(self.character_a.deal_damage())
            self.character_a.remove_health(self.character_b.deal_damage())
        elif self.character_b.agility > self.character_a.agility:
            self.character_a.remove_health(self.character_b.deal_damage())
            self.character_b.remove_health(self.character_a.deal_damage())
        else:
            character_list = [self.character_a, self.character_b]
            first = random.choice(character_list)
            if first == character_list[0]:
                self.character_b.remove_health(self.character_a.deal_damage())
                self.character_a.remove_health(self.character_b.deal_damage())
            else:
                self.character_a.remove_health(self.character_b.deal_damage())
                self.character_b.remove_health(self.character_a.deal_damage())

    def fight(self, number_of_rounds=20):
        """
        The method describing the course of the fight.
        The fight lasts 20 rounds or until one of the characters dies.

        :param number_of_rounds: Number od rounds.
        :return: None
        """
        n = 1
        while n <= number_of_rounds:
            if self.character_a.is_alive is True and self.character_b.is_alive is True:
                print(f'\nRound: {n}')
                self.round()
                n += 1
            else:
                if not self.character_a.is_alive:
                    print(f'{self.character_a.name} is killed.')
                elif not self.character_b.is_alive:
                    print(f'{self.character_b.name} is killed.')
                break
        print('\n### RESULTS ###')
        if self.character_a.health > self.character_b.health:
            print(f'{self.character_a.name} wins!!!')
        elif self.character_b.health > self.character_a.health:
            print(f'{self.character_b.name} wins!!!')
        else:
            print('DRAW!!!!')


if __name__ == '__main__':
    character01 = Knight('Optimus')
    character02 = Warrior('Megatron')
    print(character01)
    print(character02)
    battle01 = Battle(character01, character02)
    battle01.fight(5)
    print(character01)
    print(character02)
