import random
import logging


logger = logging.getLogger('Battle_logger')


class GeneralMod:
    """
    A decorator wrapping any class method by adding an integer to it.
    """
    def __init__(self, modifier):
        self.modifier = modifier

    def __call__(self, method):
        def wrapper(*args):
            return method(*args) + self.modifier
        return wrapper


class Dodge:
    """
    A decorator wrapping any class method by not calling it if a random parameter is smaller or equal than the modifier.
    """
    def __init__(self, chance):
        self.chance = chance

    def __call__(self, method):
        def wrapper(method_self, *args):
            los = random.choice(range(1, 101))
            if los <= self.chance:
                logger.info(f'{method_self.name} dodges!!!')
            else:
                return method(method_self, *args)
        return wrapper


class ReduceDamage:
    """
    A decorator wrapping any class method by adding an integer to the 'other' argument in wrapped function.
    """
    def __init__(self, modifier):
        self.modifier = modifier

    def __call__(self, method):
        def wrapper(method_self, other):
            return method(method_self, other + self.modifier)
        return wrapper
