class Money:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        if isinstance(other,str):
            raise TypeError
        n = self.a + other
        return n

    def __sub__(self, other):
        n = self.a - other
        return n

    def __mul__(self, other):
        n = self.a * other
        return n

    def __truediv__(self, other):
        if other == 0:
            raise ValueError
        n = self.a // other
        return n

    def __format__(self, other):
        line = str(self.a) + " {}".format(other)
        return line



