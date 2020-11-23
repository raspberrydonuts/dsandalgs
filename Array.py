import Sorting
# Array class that holds integers
# Performance is bad because I resize array after every operation
# Meaning that length is always equal to the true count of values
class Array:
    
    def __init__(self, length):
        self.length = length
        # python's arrays are already dynamic so the method 
        # below to create a static sized list is unnecessary
        # I'm only doing it so I can think about it as a static array
        self.contents = [None] * length

    # Linear time complexity. Have to shift elements
    def remove(self, num):
        value_removed = False
        last_index = 0
        for i in range(0, self.length, 1):
            if self.contents[i] == num:
                self.contents[i] = None
                value_removed = True
                last_index = i
                break
        if value_removed:
            for i in range(last_index, self.length-1, 1):
                self.contents[i] = self.contents[i+1]
            self.length -= 1
            self.contents[self.length] = None
            new_contents = [None] * self.length
            for i in range(0, self.length, 1):
                new_contents[i] = self.contents[i]
            self.contents = new_contents
        else:
            print("Could not find value in contents")
            return
    
    # Linear time complexity. Have to shift elements
    def insert(self, index, num):
        if index > self.length:
            print("Can't insert to index greater than length")
            return
        if index < 0:
            print("Can't insert to index less than zero")
            return
        new_contents = [None] * (self.length + 1)
        
        for i in range(0, index, 1):
            new_contents[i] = self.contents[i]
        new_contents[index] = num
        for j in range(index+1, self.length+1, 1):
            new_contents[j] = self.contents[j-1]
        self.length += 1
        self.contents = new_contents

    def find(self, num):
        for i in range(0, self.length, 1):
            if self.contents[i] == num:
                return i
        return None

    
def main():
    array = Array(5)
    i = 0
    while i < array.length:
        array.contents[i] = i
        i += 1
    print(array.contents)

    array.remove(0)
    print(array.contents)
    print(array.length)

    array.remove(3)
    print(array.contents)
    print(array.length)

    array.insert(0, 0)
    print(array.contents)
    print(array.length)

    array.insert(3, 3)
    print(array.contents)
    print(array.length)

    array.insert(5, 5)
    print(array.contents)
    print(array.length)

    array.insert(10, 1)
    array.remove(69)

    array.contents = [4, 2, 1, 6, 3, 7, 5]
    sort = Sorting.Sorting()
    sort.selection_sort(array.contents)
    print(array.contents)


if __name__ == "__main__":
    main()