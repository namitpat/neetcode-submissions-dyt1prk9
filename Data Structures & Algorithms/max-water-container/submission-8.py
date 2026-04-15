class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                height=min(heights[i],heights[j])
                width=j-i
                area=height*width
                maxArea=max(maxArea,area)

        return maxArea
                

        