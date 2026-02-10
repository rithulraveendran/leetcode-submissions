class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        mini=float('inf')
        for i in prices:
            if i<mini:
                mini=i
            elif i-mini>maxi:
                maxi=i-mini
        return maxi
