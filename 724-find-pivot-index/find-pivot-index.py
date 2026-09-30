class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        l=0
        r=sum(nums)-nums[0]
        if l==r:
            return 0
        for i in range (1,len(nums)):
            l+=nums[i-1]
            r-=nums[i]
            if l==r:
                return i
        return -1