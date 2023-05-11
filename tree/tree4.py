class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

root = Node(7)#root
root.left = Node(8) #child kiri dari root
root.right = Node(9) #child kanan dari root
root.left.left = Node(10) #child kiri kemudian ke kiri dari root
root.left.right = Node(11) #child kiri kemudian ke kanan dari root
root.left.right.left = Node(13) #child kiri dari 3
root.right.left = Node(12) #child kanan dari 3
root.right.left.left = Node(14) #child kiri dari 5
root.right.left.right = Node(15) #child kanan dari 5

print(root.PostorderTraversal(root))