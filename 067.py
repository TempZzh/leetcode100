class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        i, j = len(a)-1, len(b)-1
        carry = 0

        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += (ord(a[i]) - ord('0'))
                i -= 1
            if j >= 0:
                sum += (ord(b[j]) - ord('0'))
                j -= 1
            carry = 1 if sum > 1 else 0
            result += str(sum % 2)

        if carry: result += '1'
        return result[::-1]

if __name__ == '__main__':
    print(Solution().addBinary('11', '111'))
