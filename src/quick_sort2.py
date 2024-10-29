class MultipleMatrix:

    def __init__(self):
        self.b = {}
        self.matrix = []

    def mult_matrix(self, arr):
        for i in arr:
            self.b[i] = [x * i for x in arr]
            self.matrix.append(self.b[i])
        return self.matrix
