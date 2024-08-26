"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]: # type:ignore
        if not root:
            return []
        
        stack, result = [root], []
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children) 
        return result[::-1] 