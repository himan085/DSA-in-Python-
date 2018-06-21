#Python code to print BST keys in a given range

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def Print(root, k1, k2):
    if root is None:
        return

    if (root.data > k1) :
        Print(root.left, k1, k2)

    if root.data >= k1 and root.data <= k2 :
        print root.data,

    if root.data < k2 :
        Print(root.right, k1, k2)


k1 = 10; k2 = 25;
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)

Print(root, k1, k2)
