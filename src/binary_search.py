class PositionFinder:
    def __init__(self):
        self.max_list = None
        self.low = 0

    def bin_search(self, range_list, find_x):
        self.max_list = len(range_list) - 1
        while self.low <= self.max_list:
            mid = int((self.low + self.max_list) / 2)
            guess = range_list[mid]
            print("Trying range from list index", self.low, "to list index", self.max_list)
            if guess == find_x:
                return mid
            elif guess > find_x:
                self.max_list = mid - 1
            else:
                self.low = mid + 1
        return None
