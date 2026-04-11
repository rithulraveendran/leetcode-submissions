class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s):
            rev_val = 26 - (ord(char) - ord('a'))
            total += rev_val * (i + 1)
        return total
