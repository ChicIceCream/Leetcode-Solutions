class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1, root2):
        def get_leaves_sequence(root):
            leaves = []
            stack = [root]

            while stack:
                node = stack.pop()

                if not node.left and not node.right:
                    leaves.append(node.val)

                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)

            return leaves

        return get_leaves_sequence(root1) == get_leaves_sequence(root2)