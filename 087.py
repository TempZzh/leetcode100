class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        len_s = len(s1)
        
        F = [[[False] * (len_s + 1) for _ in range(len_s)] for _ in range(len_s)]
        
        for k in range(1, len_s + 1):
            for i in range(len_s - k + 1):
                for j in range(len_s - k + 1):
                    if k == 1:
                        F[i][j][k] = (s1[i] == s2[j])
                    else:
                        for q in range(1, k):
                            if F[i][j][k]:
                                break
                            F[i][j][k] = (F[i][j][q] and F[i + q][j + q][k - q]) or (F[i][j + k - q][q] and F[i + q][j][k - q])
        
        return F[0][0][len_s]

if __name__ == '__main__':
    # print(Solution().isScramble('great', 'rgeat'))
    # print(Solution().isScramble('abcde', 'caebd'))
    # print(Solution().isScramble('ab', 'ba'))
    print(Solution().isScramble('eebaacbcbcadaaedceaaacadccd', 'eadcaacabaddaceacbceaabeccd'))
