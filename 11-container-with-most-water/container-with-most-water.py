class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        maxarea=0
        right=len(height)-1
        while left<right:
            w=right-left
            minheight=min(height[left],height[right])
            area=minheight*w
            maxarea=max(maxarea,area)
            if (height[left]<height[right]):
                left+=1
            else:
                right-=1
        return maxarea
