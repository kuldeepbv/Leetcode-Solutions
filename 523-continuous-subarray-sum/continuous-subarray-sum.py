class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        remainder_map = {0: -1}  
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += num
            remainder = current_sum % k

            if remainder not in remainder_map:
                remainder_map[remainder] = i
            elif i - remainder_map[remainder] > 1:
                    return True

        return False           