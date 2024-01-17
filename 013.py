class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        result = 0
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
        s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
        s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')
        for char in s:
            result += translations[char]
        return result

if __name__ == '__main__':
    print(Solution().romanToInt('LVIII'))
