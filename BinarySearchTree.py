# Time Complexities:
#             Avg             Worst
# Access      O(log n)        O(n)
# Search      O(log n)        O(n)
# Insert      O(log n)        O(n)
# Delete      O(log n)        O(n)

# worst case BST is just a linked list

# Space Complexity:
# Worst - O(n)
from TreeNode import TreeNode

class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    # use for printing non decreasing order for BSTs. not for regular binary trees
    # left - root - right
    def printInOrder(self, node):
        if node is None:
            return
        # traverse left subtree
        self.printInOrder(node.left)
        # visit root
        print(node.val)
        # traverse right subtree
        self.printInOrder(node.right)

    # use for printing in non increasing order
    def printInOrderOpposite(self, node):
        if node is None:
            return
        self.printInOrderOpposite(node.right)
        print(node.val)
        self.printInOrderOpposite(node.left)


    # If you know you need to explore the roots before inspecting any leaves,
    # you pick pre-order because you will encounter all the roots before all of the leaves.
    # Use to create copy of tree
    # For example, if you want to create a replica of a tree, put the nodes in
    # an array with a pre-order traversal. Then perform an Insert operation on
    # a new tree for each value in the array. You will end up with a copy of your original tree.
    # root - left - right (hence ez copy)
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
    # left - right - root (Hence ez delete)
    def printPostOrder(self, node):
        if node is None:
            return
        # traverse left subtree
        self.printPostOrder(node.left)
        # traverse right subtree
        self.printPostOrder(node.right)
        # visit root
        print(node.val)

    # this is just traversal in BFS fashion
    def printLevelOrder(self, node):


    def insert(self, key, root):
        if root is None:
            return TreeNode(key)
        if root.val < key:
            root.right = self.insert(key, root.right)
        else:
            root.left = self.insert(key, root.left)
        return root

    # def delete(self, key, root):
    #     if root is None:
    #         return root
    #


    # node needs to be root
    def search(self, key, root):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(key, root.right)
        return self.search(key, root.left)

    # def bfs(self, key, root):
    #
    # def dfs(self, key, root):

    def isValidBSTHelper(self, root, min, max):
        if root is None:
            return True
        if root.val < min or root.val > max:
            return False
        return self.isValidBSTHelper(root.left, min, root.val - 1) and \
            self.isValidBSTHelper(root.right, root.val + 1, max)

    def isValidBST(self, root):
        return self.isValidBSTHelper(root, -(2 ** 31), 2 ** 31 - 1)

def main():
    #       4
    #     /   \
    #    2     6
    #  /  \   / \
    # 1   3  5  7
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)

    bst = BinarySearchTree(four)
    isValid = bst.isValidBST(bst.root)
    print(isValid)
    four.left = two
    two.left = one
    two.right = three
    four.right = six
    six.left = five
    six.right = seven

    print("in order ")
    bst.printInOrder(bst.root)
    print("\n\n")
    print("in order opposite? ")
    bst.printInOrderOpposite(bst.root)
    print("\n\n")
    print("pre order ")
    bst.printPreOrder(bst.root)
    print("\n\n")
    print("post order ")
    bst.printPostOrder(bst.root)

    print("\n\n")
    foundFour = bst.search(4, bst.root)
    print(foundFour.val)

    foundTwo = bst.search(2, bst.root)
    print(foundTwo.val)

    foundSeven = bst.search(7, bst.root)
    print(foundSeven.val)

    sixtyNine = TreeNode(69)

    foundInvalid = bst.search(69, bst.root)
    if foundInvalid is None:
        print("Nonexistent node not found. That's good")

    print("\n\n")
    bst.printInOrder(bst.root)
    print("\n\n")
    bst.insert(8, bst.root)
    bst.insert(2.5, bst.root)
    bst.printInOrder(bst.root)



if __name__ == "__main__":
    main()
