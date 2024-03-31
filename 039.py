# 回溯模板
# https://chat.openai.com/share/9fd9c0a6-1a56-44fd-83c5-fbad2540e66b

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        comb = []
        self.backtrack(candidates, target, [], 0, comb)
        return comb
    
    def backtrack(self, candidates, target, path, index, comb):
        if sum(path) > target:
            return
        if sum(path) == target:
            comb.append(path.copy())
            return
        
        for i in range(index, len(candidates)):
            tmp = path.copy()
            tmp.append(candidates[i])
            self.backtrack(candidates, target, tmp, i, comb)

if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
