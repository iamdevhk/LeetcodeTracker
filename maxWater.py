class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPtr=0
        rightPtr=len(height)-1
        maxWater=0
        while leftPtr<rightPtr:
            width=rightPtr-leftPtr
            h=min(height[leftPtr],height[rightPtr])
            water=width*h
            maxWater=max(water,maxWater)
            if height[leftPtr]<height[rightPtr]:
                leftPtr+=1
            else:
                rightPtr-=1
        return maxWater