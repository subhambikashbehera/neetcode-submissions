class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) - 1
        for i in heights:
            width = right - left
            height = min(heights[left],heights[right])
            area = width*height
            maxArea = max(maxArea,area)
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        return maxArea            
        