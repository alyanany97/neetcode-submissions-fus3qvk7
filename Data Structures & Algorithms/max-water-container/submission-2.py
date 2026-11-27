class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxWater = 0

        while left < right:
            if heights[left] > heights[right]:
                area = heights[right] * (right - left)
                right -= 1
            elif heights[left] < heights[right]:
                area = heights[left] * (right - left)
                left += 1
            else:
                area = heights[left] * (right - left)
                left += 1
                right -= 1
            maxWater = max(maxWater, area)
                
        return maxWater



