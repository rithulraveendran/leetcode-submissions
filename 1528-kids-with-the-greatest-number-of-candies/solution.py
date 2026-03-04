class Solution:
    def kidsWithCandies(self, candies: List[int], c: int) -> List[bool]:
        maxi=[]
        m=max(candies)
        for i in candies:
            if i+c>=m:
                maxi.append(True)
            else:
                maxi.append(False)

        return maxi
