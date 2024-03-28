from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        comb = []
        self.recursion(comb, [], nums, 0)
        return comb

    def recursion(self, comb, tmpList, nums, start):
        comb.append(tmpList.copy())
        for i in range(start, len(nums)):
            tmpList.append(nums[i])
            self.recursion(comb, tmpList, nums, i+1)
            tmpList.pop()
