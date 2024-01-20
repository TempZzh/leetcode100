from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, m*n-1
        while l < r:
            mid = (l+r-1) >> 1
            if matrix[mid//m][mid%m] < target:
                l = mid + 1
            else:
                r = mid
        return matrix[r//m][r%m] == target

if __name__ == '__main__':
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
