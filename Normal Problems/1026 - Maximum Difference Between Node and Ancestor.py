from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, min_val, max_val):
            nonlocal max_diff
            if not node:
                return

            # Update the maximum difference if found
            max_diff = max(max_diff, abs(node.val - min_val), abs(node.val - max_val))

            # Update the min and max values for the children
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            # Recursively traverse the left and right subtrees
            dfs(node.left, min_val, max_val)
            dfs(node.right, min_val, max_val)

        max_diff = 0
        dfs(root, root.val, root.val)
        return max_diff
