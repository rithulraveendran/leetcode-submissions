class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s=set()
        for i in nums1:
            if i in nums2:
                s.add(i)
        return list(s)