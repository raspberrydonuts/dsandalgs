# Time Complexities:
#             Avg       Worst
# Access      O(n)        O(n)
# Search      O(n)        O(n)
# Insert      O(1)        O(1)
# Delete      O(1)        O(1)
# Note: insertion is O(1) bc the operation is constant time (changing pointers). Unlike array where you have to shift elements. Finding the place to insert (indexing) is O(n)

# Space Complexity:
# Worst - O(n)
from Node import Node

class LinkedList:
	# head is a node
	def __init__(self, head):
		self.head = head

	def size(self):
		ptr = self.head
		counter = 0
		while ptr is not None:
			ptr = ptr.next
			counter += 1
		return counter

	def printList(self):
		ptr = self.head
		while ptr is not None:
			print(ptr.val, end=" ")
			ptr = ptr.next
		print("\n")

	def insert(self, node, index):
		counter = 0
		cur = None
		next = self.head
		while counter < index:
			cur = next
			next = next.next
			counter += 1
		if cur is not None:
			cur.next = node
		node.next = next
		if index == 0:
			self.head = node

	def insertAtEnd(self, node):
		ptr = self.head
		while ptr.next is not None:
			 ptr = ptr.next
		ptr.next = node

	def remove(self, node):
		counter = 0
		prev = Node(0)  # dummy
		cur = self.head
		while cur.val != node.val:
			prev = cur
			cur = cur.next
		if cur == self.head:
			self.head = self.head.next
		prev.next = cur.next

def main():
	zero = Node(0)
	one = Node(1)
	two = Node(2)
	three = Node(3)
	zero.next = one
	one.next = two
	two.next = three
	lst = LinkedList(zero)
	lst.printList()
	four = Node(4)
	lst.insert(four, 4)
	lst.printList()
	twoPointFive = Node(2.5)
	lst.insert(twoPointFive, 3)
	lst.printList()
	negOne = Node(-1)
	lst.insert(negOne, 0)
	lst.printList()
	lst.insertAtEnd(Node(5))
	lst.printList()
	lst.remove(twoPointFive)
	lst.printList()
	print("Size is: " + str(lst.size()))

if __name__ == "__main__":
    main()
