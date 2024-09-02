class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        final = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                final.append(nums[left] * nums[left])
                left += 1
            else:
                final.append(nums[right] * nums[right])
                right -= 1
        
        final.reverse()

        return final