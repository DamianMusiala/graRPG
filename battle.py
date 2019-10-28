# -*- coding: UTF-8 -*-

import random


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
            if self.character_a.is_alive() and self.character_b.is_alive():
                print(f'\nRound: {n}')
                self.round()
                n += 1
            else:
                if not self.character_a.is_alive():
                    print(f'{self.character_a.name} is killed.')
                elif not self.character_b.is_alive():
                    print(f'{self.character_b.name} is killed.')
                break
        print('\n### RESULTS ###')
        if self.character_a.health > self.character_b.health:
            print(f'{self.character_a.name} wins!!!')
        elif self.character_b.health > self.character_a.health:
            print(f'{self.character_b.name} wins!!!')
        else:
            print('DRAW!!!!')