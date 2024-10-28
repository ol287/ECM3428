class QuickSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        self.array = self._quick_sort(self.array)
        return self.array

    def _quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return self._quick_sort(left) + middle + self._quick_sort(right)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
quick_sorter = QuickSort(arr)
sorted_arr = quick_sorter.sort()
print("Sorted array:", sorted_arr)
