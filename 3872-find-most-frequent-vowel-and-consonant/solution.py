class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = "aeiou"
        x = {}
        y = {}
        for char in s:
            if char in v:
                x[char] = x.get(char, 0) + 1
            else:
                y[char] = y.get(char, 0) + 1
        mx = max(x.values()) if x else 0
        my = max(y.values()) if y else 0
        return mx + my

