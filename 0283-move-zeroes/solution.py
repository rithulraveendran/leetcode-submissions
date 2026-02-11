class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count=0
        for i in range(0,len(nums)):
            if nums[i]==0:
                count+=1
        while 0 in nums:
            nums.remove(0)
        while count!=0:
            nums.append(0)
            count-=1
