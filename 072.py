from typing import Dict, Tuple

class Solution:
    def helper(self, word1: str, word2: str, i: int, j: int, memo: Dict[Tuple, int]) -> int:
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        
        if (i,j) not in memo:
            if word1[i] == word2[j]:
                ans = self.helper(word1, word2, i+1, j+1, memo)
            else:
                insert = 1 + self.helper(word1, word2, i, j+1, memo)
                delete = 1 + self.helper(word1, word2, i+1, j, memo)
                replace = 1 + self.helper(word1, word2, i+1, j+1, memo)
                ans = min(insert, delete, replace)
            memo[(i,j)] = ans
        return memo[(i,j)]

    def minDistance(self, word1: str, word2: str) -> int:
        return self.helper(word1, word2, 0, 0, {})


if __name__ == '__main__':
    print(Solution().minDistance('dinitrophenylhydrazine', 'acetylphenylhydrazine'))
