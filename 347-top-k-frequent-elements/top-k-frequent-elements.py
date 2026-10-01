from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hmap=defaultdict(int)
        for i in nums:
            hmap[i]+=1

        arr=[[] for _ in range(len(nums)+1)]
        for i,j in hmap.items():
            arr[j].append(i)
        
        res=[]
        for i in range(len(arr)-1,0,-1):
            for j in (arr[i]):
                res.append(j)
                if len(res)==k:
                    return res