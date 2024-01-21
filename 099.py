# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.firstElement: TreeNode = None
        self.secondElement: TreeNode = None
        self.prevElement = TreeNode(-2**63)

        self.traverse(root)
        tmp = self.firstElement.val
        self.firstElement.val = self.secondElement.val
        self.secondElement.val = tmp
    
    def traverse(self, root: Optional[TreeNode]):
        if root == None:
            return
        self.traverse(root.left)
        if self.firstElement == None and self.prevElement.val >= root.val:
            self.firstElement = self.prevElement
        if self.firstElement != None and self.prevElement.val >= root.val:
            self.secondElement = root
        self.prevElement = root
        self.traverse(root.right)
