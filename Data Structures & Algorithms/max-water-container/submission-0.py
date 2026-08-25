class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) - 1
        for i in heights:
            width = right - left
            height = min(heights[right],heights[left])
            area = width * height
            maxArea = max(area,maxArea)
            if heights[left] > heights[right]:
                right -=1
            else:
                left +=1    
        return maxArea        