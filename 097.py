class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        DP = [ [False for _ in range(len(s2)+1)] for _ in range(len(s1)+1) ]

        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    DP[i][j] = True
                elif i == 0:
                    DP[i][j] = ( DP[i][j-1] and s2[j-1] == s3[i+j-1] )
                elif j == 0:
                    DP[i][j] = ( DP[i-1][j] and s1[i-1] == s3[i+j-1] )
                else:
                    DP[i][j] = ( DP[i-1][j] and s1[i-1] == s3[i+j-1] ) or ( DP[i][j-1] and s2[j-1] == s3[i+j-1] )

        return DP[len(s1)][len(s2)]


if __name__ == '__main__':
    print(Solution().isInterleave('a', '', 'a'))
