class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for idx in range(len(nums) - 1):
            if nums[idx] % 2 == nums[idx + 1] % 2:
                return False
        return True