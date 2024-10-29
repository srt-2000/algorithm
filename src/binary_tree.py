class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def pre_order(self, node):
        if node:
            print(node.val, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.val, end=' ')

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.val, end=' ')
            self.in_order(node.right)
