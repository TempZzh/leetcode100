from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        reach = 0
        while i < len(nums) and i <= reach:
            reach = max(i + nums[i], reach)
            i += 1
        return i == len(nums)

if __name__ == '__main__':
    print(Solution().canJump([3, 2, 1, 0, 4]))
