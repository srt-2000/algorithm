class SortFast:

    def __init__(self, data):
        self.data = data
        self.smallest = data[0]
        self.smallest_ind = 0
        self.new_arr =[]

    def find_smallest(self):
        for i in range(1, len(self.data)):
            if self.data[i] < self.smallest:
                self.smallest = self.data[i]
                self.smallest_ind = i
        return self.smallest_ind

    def selection_sort(self):
        for i in range(len(self.data)):
            self.smallest = self.find_smallest()
            self.new_arr.append(self.data.pop(self.smallest))
        return self.new_arr

print("Hello!\nI'm the classic sort (On^2) algorithm.\n")
data_arr = [int(n) for n in input("Enter the list numbers you want to sort:").split()]
fsort_obj = SortFast(data_arr)
print(fsort_obj.selection_sort())