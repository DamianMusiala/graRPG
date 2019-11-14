import random
import decorators
import equipment
import logging


logger = logging.getLogger('Battle_logger')


class Character:
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
        self.equipment = {'head': equipment.Item,
                           'torso': equipment.Item,
                           'foot': equipment.Item,
                           'right_hand': equipment.Item,
                           'left_hand': equipment.Item}

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
        return self.final_stats()['health'] > 0

    def remove_health(self, other):
        """
        Modifies in place health and is_alive parameters
        :param other: Damage dealt by opponent
        :type other: integer
        :return: None
        """
        equipment_bonus = 0
        for i in self.equipment.values():
            equipment_bonus += i.remove_health
        damage_received = other + equipment_bonus if other + equipment_bonus >= 0 else 0
        self.health -= damage_received
        logger.info(f'{self.name} loses {damage_received} health points. Equipement bonus = {equipment_bonus}')
        if self.health < 1:
            self.health = 0
            logger.info(f'{self.name} is killed.')

    def deal_damage(self):
        """
        Calculates and returns the value of damage. Draws a value from 1 to 10.
        :return: damage (integer)
        """
        equipment_damage = 0
        for i in self.equipment.values():
            equipment_damage += i.deal_damage
        damage = random.randint(1, 10) + equipment_damage
        logger.info(f'{self.name} deals {damage} damage. Equipment damage = {equipment_damage}')
        return damage

    def select_equipement(self, box):
        """
        Draw three values ​​from the given list.
        """
        random.shuffle(box)
        for i in box[:3]:
            for j in self.equipment:
                if i.body == j:
                    self.equipment[j] = i
                else:
                    continue

    def final_stats(self):
        """
        Collecting final character and equipment statistics
        :return: statistics dictionary
        """
        final_agility = 0
        final_constitution = 0
        final_health = 0
        for i in self.equipment.values():
            final_agility += i.agility
            final_constitution += i.constitution
            final_health += i.health
        result = {'name': self.name,
                  'agility': self.agility + final_agility,
                  'constitution': self.constitution + final_constitution,
                  'health': self.health + final_health,
                  'equipment': self.equipment}
        return result

    def __str__(self):
        return f"///\nName: {self.name} > " \
            f"Health: {self.final_stats()['health']} > " \
            f"Agility: {self.final_stats()['agility']} > " \
            f"Constitution: {self.final_stats()['constitution']}\n" \
            f"Equipment: {self.final_stats()['equipment']}"


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

    @decorators.GeneralMod(10)
    def constitution(self):
        return Character.constitution()

    @decorators.GeneralMod(2)
    def deal_damage(self):
        logger.info(f'{self.name} deals 2 additional damage points!!!')
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

    @decorators.GeneralMod(-10)
    def agility(self):
        return Character.agility()

    @decorators.ReduceDamage(-2)
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

    @decorators.GeneralMod(10)
    def agility(self):
        return Character.agility()

    @decorators.Dodge(25)
    def remove_health(self, other):
        return Character.remove_health(self, other)


if __name__ == '__main__':
    char01 = Warrior('Damian')
    logger.info(char01.final_stats())
    standard_eq = [equipment.Helm(), equipment.Armor(), equipment.Sword(), equipment.Shield(), equipment.Shoes()]
    char01.select_equipement(standard_eq)
    for i in char01.equipment.values():
        logger.info(i)
    logger.info(char01.final_stats())
