from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, tmp):
            if len(tmp) == n * 2:
                x.append(tmp)
                return
            if left < n:
                dfs(left + 1, right, tmp + '(')
            if left > right:
                dfs(left, right + 1, tmp + ')')
        
        x = []
        dfs(0, 0, '')
        return x

if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
