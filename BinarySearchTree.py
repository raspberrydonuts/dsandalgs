# Time Complexities:
#             Avg             Worst
# Access      O(log n)        O(n)
# Search      O(log n)        O(n)
# Insert      O(log n)        O(n)
# Delete      O(log n)        O(n)

# worst case BST is just a linked list

# Space Complexity:
# Worst - O(n)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    # use for printing non decreasing order
    def printInOrder(self, node):
        if node is None:
            return
        # traverse left subtree
        self.printInOrder(node.left)
        # visit root
        print(node.val)
        # traverse right subtree
        self.printInOrder(node.right)


    # If you know you need to explore the roots before inspecting any leaves,
    # you pick pre-order because you will encounter all the roots before all of the leaves.
    # Use to create copy of tree
    # For example, if you want to create a replica of a tree, put the nodes in
    # an array with a pre-order traversal. Then perform an Insert operation on
    # a new tree for each value in the array. You will end up with a copy of your original tree.
    def printPreOrder(self, node):
        if node is None:
            return
        # visit root
        print(node.val)
        # traverse left subtree
        self.printPreOrder(node.left)
        # traverse right subtree
        self.printPreOrder(node.right)

    # If you know you need to explore all the leaves before any nodes,
    # you select post-order because you don't waste any time inspecting roots in search for leaves.
    # Used to delete a tree from leaf to root
    def printPostOrder(self, node):
        if node is None:
            return
        # traverse left subtree
        self.printPostOrder(node.left)
        # traverse right subtree
        self.printPostOrder(node.right)
        # visit root
        print(node.val)
    #
    # def insert(self, node):
    #
    # def delete(self, node):
    #
    # def search(self, key):
    #
    # def isValidBST(self):

def main():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)

    bst = BinarySearchTree(four)
    four.left = two
    two.left = one
    two.right = three
    four.right = six
    six.left = five
    six.right = seven

    bst.printInOrder(bst.root)
    print("\n\n")
    bst.printPreOrder(bst.root)
    print("\n\n")
    bst.printPostOrder(bst.root)

if __name__ == "__main__":
    main()
