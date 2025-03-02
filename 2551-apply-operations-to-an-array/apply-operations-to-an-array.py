class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        final = []
        for num in nums:
            if num != 0:
                final.append(num)

        for i in range(len(nums) - len(final)):
            final.append(0)

        return final