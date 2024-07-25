from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        if (a+b+c+d) == len(s):
                            A = int(s[0:a])
                            B = int(s[a:(a+b)])
                            C = int(s[(a+b):(a+b+c)])
                            D = int(s[(a+b+c):(a+b+c+d)])
                            if A <= 255 and B <= 255 and C <= 255 and D <= 255:
                                tmp = str(A) + '.' + str(B) + '.' + str(C) + '.' + str(D)
                                if len(tmp) == len(s) + 3:
                                    ret.append(tmp)
        return ret


if __name__ == '__main__':
    print(Solution().restoreIpAddresses('101023'))
