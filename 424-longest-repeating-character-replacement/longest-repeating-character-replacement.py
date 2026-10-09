class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        m = 0
        f = 0
        for r, c in enumerate(s):
            d[c] = d.get(c, 0) + 1
            f = max(f, d[c])
            if (r - l + 1) - f > k:
                d[s[l]] -= 1
                l += 1
            m = max(m, r - l + 1)
        return m