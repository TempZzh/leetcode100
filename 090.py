from typing import List
import copy

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums.sort()
        i = 0
        while i < len(nums):
            count = 0
            while (count + i < len(nums)) and (nums[count+i] == nums[i]):
                count += 1
            previousN = len(result)
            for j in range(previousN):
                instance = list(result[j])
                for _ in range(count):
                    instance.append(nums[i])
                    result.append(list(instance))
            i += count
        return result

if __name__ == '__main__':
    print(Solution().subsetsWithDup([1, 2, 2]))
    print(Solution().subsetsWithDup([0]))
