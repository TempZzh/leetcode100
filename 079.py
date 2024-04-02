from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(y, x, i):
            if i == len(word):
                return True
            
            if y < 0 or x < 0 or y == len(board) or x == len(board[y]):
                return False
            
            if board[y][x] != word[i]:
                return False
            
            tmp = board[y][x]
            board[y][x] = '#'
            find = dfs(y, x+1, i+1) or dfs(y, x-1, i+1) or dfs(y+1, x, i+1) or dfs(y-1, x, i+1)
            board[y][x] = tmp

            return find

        for y in range(0, len(board)):
            for x in range(0, len(board[y])):
                if dfs(y, x, 0):
                    return True
        return False

if __name__ == '__main__':
    print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED'))
