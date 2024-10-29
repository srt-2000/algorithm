class FactorialCalculate:

    def fa_calc(self, x):
        if x == 1:
            return 1
        else:
            return x * self.fa_calc(x - 1)
