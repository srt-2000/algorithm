class Sqr:

    def __init__(self):
        self.result = None

    def sqr_arr(self, a_):
        self.result = map(lambda x: x ** 2, a_)
        return list(self.result)
