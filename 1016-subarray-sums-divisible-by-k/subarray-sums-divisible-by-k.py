class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_dict = {0: 1}
        current_sum = 0
        final_count = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            remainder = current_sum % k

            if remainder < 0:
                remainder += k

            if remainder not in remainder_dict:
                remainder_dict[remainder] = 1
            else:
                final_count += remainder_dict[remainder]
                remainder_dict[remainder] += 1
        
        return final_count