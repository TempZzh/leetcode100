from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base case: if the list is empty, return an empty list
        if not nums:
            return [[]]
        
        permutations = []

        for i in range(len(nums)):
            for remaining_permutations in self.permute(nums[:i] + nums[i+1:]):
                permutations.append([nums[i]] + remaining_permutations)

        return permutations

if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
