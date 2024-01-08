from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        i = 0
        while i < len(nums):
            num = nums[i]
            target = -num
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    triple = [num, nums[left], nums[right]]
                    res.append(triple)
                    while left < right and nums[left] == triple[1]:
                        left += 1
                    while left < right and nums[right] == triple[2]:
                        right -= 1
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            i += 1
        return res

if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1,2,-1,-4]))
