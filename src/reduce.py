import functools


class RedFun:

    def __init__(self):
        self.lst = []

    def arr_sum(self, lst):
        self.lst = lst
        return functools.reduce(lambda a, b: a + b, self.lst)

    def arr_max(self, lst):
        self.lst = lst
        return functools.reduce(lambda a, b: a if a > b else b, self.lst)
