class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            temp_area = min(height[left], height[right]) * (right - left)
            if temp_area > area:
                area = temp_area
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            
        return area