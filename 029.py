class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        a, b, result = abs(dividend), abs(divisor), 0
        while a >= b:
            q = 0
            while a > (b<<(q+1)):
                q += 1
            result += (1<<q)
            a -= (b<<q)
        return sign * result
