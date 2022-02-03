from functools import total_ordering


@total_ordering
class Numbers:
    __slots__ = 'val'

    def __repr__(self):
        return str(self.val)

    def __eq__(self, other):
        return self.val == other

    def __lt__(self, other):
        return self.val < other

    def __abs__(self):
        return abs(self.val)

    def __add__(self, other):
        return self.val+other

    def __and__(self, other):
        return self.val & other

    def __bool__(self):
        return self.val != 0

    def __ceil__(self):
        return self.val

    def __divmod__(self, other):
        return divmod(self.val, other)

    def __float__(self):
        return float(self.val)

    def __floordiv__(self, other):
        return self.val//other

    def __floor__(self):
        return self.val

    def __hash__(self):
        return hash(self.val)

    def __int__(self):
        return self.val

    def __invert__(self):
        return ~self.val

    def __lshift__(self, other):
        return self.val << other

    def __mod__(self, other):
        return self.val % other

    def __mul__(self, other):
        return self.val*other

    def __neg__(self):
        return -self.val

    def __or__(self, other):
        return self.val | other

    def __pos__(self):
        return +self.val

    def __pow__(self, value, mod):
        return pow(self.val, value, mod)

    def __round__(self):
        return self.val

    def __rshift__(self, other):
        return self.val >> other

    def __sub__(self, other):
        return self.val-other

    def __truediv__(self, other):
        return self.val/other

    def __trunc__(self):
        return self.val

    def __xor__(self, other):
        return self.val ^ other


class Zero(Numbers):
    val = 0


class One(Numbers):
    val = 1


class Two(Numbers):
    val = 2


class Three(Numbers):
    val = 3


class Four(Numbers):
    val = 4


class Five(Numbers):
    val = 5


class Six(Numbers):
    val = 6


class Seven(Numbers):
    val = 7


class Eight(Numbers):
    val = 8


class Nine(Numbers):
    val = 9

