# -*- coding: UTF-8 -*-


class AttrDisplay:
    """
    Udostępnia dziedziczoną metodę przeciążania wyświetlania, która pokazuje instancje z ich nazwami klas, a także parę
    nazwa=wartość dla każdego atrybutu przechowanego w samej instancji (ale nie atrybutów odziedziczonych po klasach).
    Można ją wmieszać w dowolną klasę i będzie działała na dowolnej instancji.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f'{key}={getattr(self, key)}')
        return ', '.join(attrs)

    def __str__(self):
        return f'[{self.__class__.__name__}: {self.gatherAttrs()}]'


if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 100


    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)
