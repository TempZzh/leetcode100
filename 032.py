class Solution:
    def longestValidParentheses(self, s: str) -> int:

        n = len(s)
        longest = 0
        stack = []

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    if s[stack[-1]] == '(':
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
        
        if not stack:
            longest = n
        else:
            a = n
            b = 0
            while stack:
                b = stack.pop()
                longest = max(longest, a-b-1)
                a = b
            longest = max(longest, a)

        return longest

if __name__ == '__main__':
    print(Solution().longestValidParentheses('()()()'))
