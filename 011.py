from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1

        while left < right:
            water = max(water, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return water


class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            water = max(water, (right - left) * h)
            while height[left] <= h and left < right:
                left += 1
            while height[right] <= h and left < right:
                right -= 1

        return water
