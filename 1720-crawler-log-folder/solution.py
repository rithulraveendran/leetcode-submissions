class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for i in logs:
            if i=='../':
                count = max(0, count - 1)
            elif i=='./':
                pass
            else:
                count+=1
            
        return count
