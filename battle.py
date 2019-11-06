"""
gracz powinien się składac z ekwipunku i charakteru
ekwipunek nie opakowuje charakteru w oczekiwany sposób (albo ja tego nie potrafię)
trzeba zastosować inny wzorzec projektowy niż dekorator do stworzenia gracza
na razie gracz to tylko charakter :/
"""


import random
import characters
import equipment


class Battle:
    """
    Battle class.
    Battle between two characters.

    :param players: Player list.
    :method number_of_players: Calculates number oof players.
    :method order: Determines the order of movement.
    :method round: Specifies the behavior during the round.
    :method fight: Manages the number of rounds and indicates the winner.
    """
    def __init__(self, players):
        """
        Battle class constructor.
        :param players: Player list.
        """
        self.players = players

    def number_of_players(self):    # w założeniu, że w przyszłości będzie wiecej graczy
        """
        :return: Lenght of the player list = number of players
        """
        return len(self.players)

    def order(self):
        """
        A character with a higher agility parameter is the first player.
        If the agility parameters are equal, the method randomizes the first player..
        :return: Modyfied player list.
        """
        if self.players[0].final_stats()['agility'] != self.players[1].final_stats()['agility']:
            self.players = sorted(self.players, key=lambda player: player.agility, reverse=True)
        else:
            random.shuffle(self.players)
        return self.players

    def round(self):
        """
        The method describing the course of the round.
        A character with a higher agility parameter starts the round and deals damage.
        Then the opponent deals damage (if he can).
        If the agility parameters are equal, the method randomizes the starting character.
        :return: None
        """
        arena = self.order()

        arena[1].remove_health(arena[0].deal_damage())
        if arena[1].is_alive():
            arena[0].remove_health(arena[1].deal_damage())

    def fight(self):
        """
        The method describing the course of the fight.
        If both of the players are alive a round can be made.
        :return: None
        """
        # displaying initial values
        for player in self.players:
            print(player)

        n = 1
        while True:
            if self.players[0].is_alive() and self.players[1].is_alive():
                print(f'\nRound: {n}')
                self.round()
                n += 1
            else:
                break
        print('\n### RESULTS ###')
        if not self.players[0].is_alive() and not self.players[1].is_alive():
            print('DRAW!!!')
        for player in self.players:
            if player.is_alive():
                print(f'{player.name} wins!!!')

        # displaying end values
        for player in self.players:
            print(player)


if __name__ == '__main__':
    standard_equipement = [equipment.Helm(),
                           equipment.Armor(),
                           equipment.Shoes(),
                           equipment.Sword(),
                           equipment.Shield()]
    warrior1 = characters.Warrior('WARRIOR 1')
    warrior1.select_equipement(standard_equipement)
    warrior2 = characters.Warrior('WARRIOR 2')
    warrior2.select_equipement(standard_equipement)
    knight1 = characters.Knight('KNIGHT 1')
    knight1.select_equipement(standard_equipement)
    knight2 = characters.Knight('KNIGHT 2')
    knight2.select_equipement(standard_equipement)
    thief1 = characters.Thief('THIEF 1')
    thief1.select_equipement(standard_equipement)
    thief2 = characters.Thief('THIEF 2')
    thief2.select_equipement(standard_equipement)
    warriorVSwarrior = [warrior1, warrior2]
    warriorVSknight = [warrior1, knight1]
    warriorVSthief = [warrior1, thief1]
    knightVSknight = [knight1, knight2]
    knightVSthief = [knight1, thief1]
    thiefVSthief = [thief1, thief2]
    battle = Battle(warriorVSthief)
    battle.fight()
