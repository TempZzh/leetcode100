# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        stack = []
        pre = None
        while root != None or stack:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre != None and root.val <= pre.val:
                return False
            pre = root
            root = root.right
        return True

if __name__ == '__main__':
    pass
