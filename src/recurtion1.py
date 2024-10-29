class CountDown:

    def __init__(self):
        self.range_of_row = None

    def down_row(self, range_of_row):
        self.range_of_row = range_of_row
        print(self.range_of_row)
        if self.range_of_row <= 0:
            return self.range_of_row
        else:
            return self.down_row(range_of_row - 1)
