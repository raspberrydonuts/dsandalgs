class Sorting:
    @staticmethod
    def selection_sort(lst):
        for i in range(len(lst)):
            min_index = i  # set first unsorted element as the minimum
            for j in range(i+1, len(lst)):  # for each unsorted element
                # if element is smaller than current minimum, update
                if lst[min_index] > lst[j]:  # check if there's new minimum
                    min_index = j       
            # swap minimum with first unsorted position
            lst[i], lst[min_index] = lst[min_index], lst[i]
