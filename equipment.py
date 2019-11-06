# -*- coding: UTF-8 -*-


class Item:
    body = None
    agility = 0
    constitution = 0
    health = 0
    remove_health = 0
    deal_damage = 0


class Armor(Item):
    body = 'torso'
    agility = 0
    constitution = 0
    health = 0
    remove_health = -5
    deal_damage = 0


class Helm(Item):
    body = 'head'
    agility = 0
    constitution = 0
    health = 0
    remove_health = -3
    deal_damage = 0


class Sword(Item):
    body = 'right_hand'
    agility = 0
    constitution = 0
    health = 0
    remove_health = 0
    deal_damage = 5


class Shield(Item):
    body = 'left_hand'
    agility = 0
    constitution = 0
    health = 0
    remove_health = -3
    deal_damage = 1


class Shoes(Item):
    body = 'foot'
    agility = 10
    constitution = 0
    health = 0
    remove_health = -1
    deal_damage = 0
