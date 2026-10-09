class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[l],nums[i]=nums[i],nums[l]
                l+=1