class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d=defaultdict(int)
        l=[]
        for i in nums1:
            d[i]+=1
        for j in nums2:
            if j in d.keys() and d[j]>=1:
                l.append(j)
                d[j]-=1
        return l
            