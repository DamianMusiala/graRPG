import random
import characters
import equipment
import os
import platform
import logging


logger = logging.getLogger('Battle_logger')


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
            logger.info(player)

        n = 1
        while True:
            if self.players[0].is_alive() and self.players[1].is_alive():
                logger.info(f'\nRound: {n}')
                self.round()
                n += 1
            else:
                break
        logger.info('\n### RESULTS ###')
        if not self.players[0].is_alive() and not self.players[1].is_alive():
            logger.info('DRAW!!!')
        for player in self.players:
            if player.is_alive():
                logger.info(f'{player.name} wins!!!')

        # displaying end values
        for player in self.players:
            logger.info(player)


def logger_sets():
    if platform.platform().startswith('Windows'):
        logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'rpg.log')
    else:
        logging_file = os.path.join(os.getenv('HOME'), 'rpg.log')
    # create logger
    logger = logging.getLogger('Battle_logger')
    logger.setLevel(logging.INFO)
    # create file handler and set level to debug
    file_handler = logging.FileHandler(logging_file, mode='w')
    file_handler.setLevel(logging.INFO)
    # create formatter
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
    # add formatter to file_handler
    file_handler.setFormatter(formatter)
    # add file_handler to logger
    logger.addHandler(file_handler)


if __name__ == '__main__':
    logger_sets()
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