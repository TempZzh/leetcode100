
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        rot = lo
        lo, hi, n = 0, len(nums) - 1, len(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            realMid = (mid + rot) % n
            if nums[realMid] == target:
                return realMid
            elif nums[realMid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


if __name__ == '__main__':
    print(Solution().search([4,5,6,7,0,1,2], 0))
