class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=sum(nums[:k])
        m=l
        for i in range(k,len(nums)):
            l=l+nums[i]-nums[i-k]
            if l>m:
                m=l
        return m/k