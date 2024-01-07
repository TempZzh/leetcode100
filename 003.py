class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
             return 0
        mem = {}
        max = 0
        start = 0
        end = 0
        for i, c in enumerate(s):
            if c in mem and mem[c] >= start:
                if end - start + 1 > max:
                    max = end - start + 1
                start = mem[c] + 1
            end = i
            mem[c] = i
        if end - start + 1 > max:
                    max = end - start + 1
        return max

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(' '))
