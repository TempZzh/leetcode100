# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generateSubTrees(1, n)
    
    def generateSubTrees(self, start: int, end: int) -> List[Optional[TreeNode]]:
        result = []
        if start > end:
            result.append(None)
            return result
        for i in range(start, end+1):
            leftSubTrees = self.generateSubTrees(start, i-1)
            rightSubTrees = self.generateSubTrees(i+1, end)
            for left in leftSubTrees:
                for right in rightSubTrees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    result.append(root)
        return result
