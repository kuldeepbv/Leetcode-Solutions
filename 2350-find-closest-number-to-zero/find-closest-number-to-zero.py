class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        final = nums[0]
        for num in nums[1:]:
            current = abs(num - 0)
            if current <= abs(final):
                final = num
            else:
                continue
        return final