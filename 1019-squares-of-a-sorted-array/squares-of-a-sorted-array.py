class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        final = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                final[i] = nums[left] * nums[left]
                left += 1
            else:
                final[i] = nums[right] * nums[right]
                right -= 1

        return final