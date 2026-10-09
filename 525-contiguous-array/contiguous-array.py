class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        s = 0
        m = 0
        for i, v in enumerate(nums):
            s += 1 if v == 1 else -1
            if s in d:
                m = max(m, i - d[s])
            else:
                d[s] = i
        return m