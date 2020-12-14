import heapq

def main():
    arr = [3, 1, 2, 9 ,8]
    heapq.heapify(arr) # puts smallest at index 0
    print(arr)
    heapq.heappush(arr, 0) # replaces index 0 if new smallest. otherwise just appends
    print(arr)
    heapq.heappop(arr) # pops smallest item and returns it
    print(arr)
    heapq.heappushpop(arr, 4) # simulatenously appends 4 and pops smallest item and returns it
    # heappushpop is like heappush then heappop but more efficient
    # note that heap size can change (if empty, you'll get back the element you pushed)
    print(arr)
    # pop and return smallest item, and then push new element
    # guarantees heap size won't change
    heapq.heapreplace(arr, 2)
    print(arr)
    print(heapq.nlargest(3, arr)) # prints 3 largest in arr
    print(heapq.nsmallest(3, arr)) # prints 3 smallest in arr

    # in order to use a max heap, you can invert all the values and use a min heap
    
if __name__ == "__main__":
    main()
