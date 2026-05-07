class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        minHeight = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            if heights[left] < heights[right]:
                minHeight = heights[left]
                area = (right - left) * minHeight
                left +=1
            else:
                minHeight = heights[right]
                area = (right - left) * minHeight
                right -= 1

            maxArea = max(maxArea, area)
        return maxArea
            


