class Summator:
    def array_sum(self, arr):
        if not arr:
            return 0
        else:
            return arr.pop(0) + self.array_sum(arr)
