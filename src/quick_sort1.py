class QuickSort:
    def sorted(self, arr):
        if len(arr) < 2:
            return arr
        else:
            pivot = arr[int(len(arr) / 2)]
            less = [i for i in arr if i < pivot]
            greater = [i for i in arr if i > pivot]
            return self.sorted(less) + [pivot] + self.sorted(greater)
