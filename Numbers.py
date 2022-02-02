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


class Zero(Numbers):
    val = 0

