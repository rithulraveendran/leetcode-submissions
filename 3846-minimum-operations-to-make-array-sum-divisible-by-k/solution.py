class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total=sum(nums)
        rem=total%k
        return rem    
