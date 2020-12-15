class HashTable:
    def __init__(self, length):
        # creates hash table as nested list
        self.table = [[] for _ in range(length)]

    # Function to display hashtable
    def display_hash(self):

    	for i in range(len(self.table)):
    		print(i, end = " ")

    		for j in self.table[i]:
    			print("-->", end = " ")
    			print(j, end = " ")

    		print()

    # Hashing Function to return
    # key for every value.
    def hash(self, keyvalue):
    	return keyvalue % len(self.table)


    # Insert Function to add
    # values to the hash table
    def insert(self, keyvalue, value):

    	hash_key = self.hash(keyvalue)
    	self.table[hash_key].append(value)

# Driver Code
if __name__ == '__main__':
    hashtable = HashTable(10)
    hashtable.insert(10, 'Allahabad')
    hashtable.insert(25, 'Mumbai')
    hashtable.insert(20, 'Mathura')
    hashtable.insert(9, 'Delhi')
    hashtable.insert(21, 'Punjab')
    hashtable.insert(21, 'Noida')
    hashtable.display_hash()
