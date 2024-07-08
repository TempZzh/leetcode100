from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

if __name__ == '__main__':
    nums = [1, 2, 3]
    Solution().removeDuplicates(nums)
    print(nums)
