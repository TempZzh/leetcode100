from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, numa in enumerate(nums):
            for j, numb in enumerate(nums):
                if numa + numb == target and i != j:
                    return [i, j]
        return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, num in enumerate(nums):
            if target-num in mem:
                return[i, mem[target-num]]
            mem[num] = i
        return []

if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15], 9))
