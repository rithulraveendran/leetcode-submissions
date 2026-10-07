class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        n=len(arr)
        c=0
        curr=sum(arr[:k])
        avg=curr//k
        if avg>=threshold:
            c+=1
        for i in range(k,n):
            curr-=arr[i-k]
            curr+=arr[i]
            avg=curr//k
            if avg>=threshold:
                c+=1
        return c