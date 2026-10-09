class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        c = 0
        s = 0
        d = {0: 1}
        for n in nums:
            s = (s + n) % k
            if s < 0:
                s += k
            if s in d:
                c += d[s]
                d[s] += 1
            else:
                d[s] = 1
        return c