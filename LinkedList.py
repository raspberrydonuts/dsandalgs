# Time Complexities:
#             Avg       Worst
# Access      O(n)        O(n)
# Search      O(n)        O(n)
# Insert      O(1)        O(1)
# Delete      O(1)        O(1)
# Note: insertion is O(1) bc the operation is constant time (changing pointers). Unlike array where you have to shift elements. Finding the place to insert (indexing) is O(n)

# Space Complexity:
# Worst - O(n)


class Node:
	def __init__(self, val=0, next=None):
    	self.val = val
        self.next = next
        
        
class LinkedList:
	def __init__(self, head):
    	self.head = head
        
    def printList(self):
    
    def insert(self, index):

	def insertAtEnd(self):
    
    def remove(self, index):
    
    def copy(self):
    
