class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        rank = {}
        for i in range(len(sorted_nums)):
            num = sorted_nums[i]
            if num not in rank:
                rank[num] = i
        result = []
        for i in range(len(nums)):
            result.append(rank[nums[i]])
        return result
