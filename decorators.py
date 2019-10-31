import random


def general_mod(modifier):
    def wrapper(func):
        def inner(self, *attrs):
            return func(self, *attrs) + modifier
        return inner
    return wrapper


def dodge(chance):
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
    def wrapper(func):
        def inner(self, other):
            return func(self, other + modifier)
        return inner
    return wrapper
