import random


def general_mod(modifier):
    """
    A decorator wrapping any class method by adding an integer to it.
    :param modifier: integer
    :return: wrapped function
    """
    def wrapper(func):
        def inner(self, *attrs):
            return func(self, *attrs) + modifier
        return inner
    return wrapper


def dodge(chance):
    """
    A decorator wrapping any class method by not calling it if a random parameter is smaller or equal than the modifier.
    :param chance: modifier
    :return: wrapped function
    """
    def wrapper(func):
        def inner(self, *attrs):
            los = random.choice(range(1, 101))
            if los <= chance:
                print(f'{self.name} dodges!!!')
            else:
                return func(self, *attrs)
        return inner
    return wrapper


def reduce_damage(modifier):
    """
    A decorator wrapping any class method by adding an integer to the 'other' argument in wrapped function.
    :param modifier: integer
    :return: wrapped function
    """
    def wrapper(func):
        def inner(self, other):
            return func(self, other + modifier)
        return inner
    return wrapper
