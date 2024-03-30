# https://chat.openai.com/share/9fd9c0a6-1a56-44fd-83c5-fbad2540e66b

from typing import List


class Solution:
    dict = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        combinations = []
        self.dfs(digits, 0, '', combinations)
        return combinations

    def dfs(self, digits, index, path, combinations):
        if index == len(digits):
            combinations.append(path)
            return
        
        for x in self.dict[digits[index]]:
            self.dfs(digits, index + 1, path + x, combinations)

if __name__ == '__main__':
    print(Solution().letterCombinations('2345'))
