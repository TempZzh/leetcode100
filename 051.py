from typing import List

# No.131 https://leetcode.cn/problems/palindrome-partitioning/description/
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:

#         def isPalindrome(str, l, r):
#             if l == r:
#                 return True
#             while l < r:
#                 if str[l] != str[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             return True
        
#         def backTrack(s, start):
#             if len(currList) > 0 and start >= len(s):
#                 res.append(currList.copy())
#                 return
#             for i in range(start, len(s)):
#                 if isPalindrome(s, start, i):
#                     currList.append(s[start:i+1])
#                     backTrack(s, i+1)
#                     currList.pop()
        
        
#         res = []
#         currList = []
#         backTrack(s, 0)
#         return res

# if __name__ == '__main__':
#     print(Solution().partition('axab'))

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        checkerboard = ['.'*n] * n

        def isValid(row, col):
            for i in range(row):
                if checkerboard[i][col] == 'Q':
                    return False
            
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if checkerboard[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if checkerboard[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True

        def backTrack(row):
            if row == n:
                res.append(checkerboard.copy())
                return
            for col in range(n):
                if isValid(row, col):
                    checkerboard[row] = checkerboard[row][:col] + 'Q' + checkerboard[row][col+1:]
                    backTrack(row + 1)
                    checkerboard[row] = checkerboard[row][:col] + '.' + checkerboard[row][col+1:]

        backTrack(0)
        return res

if __name__ == '__main__':
    print(Solution().solveNQueens(4))
