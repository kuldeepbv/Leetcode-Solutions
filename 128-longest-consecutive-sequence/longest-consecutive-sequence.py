class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        sorted_nums = sorted(nums)
        max_length = 0
        check_element = sorted_nums[0]
        longest = 1

        for num in sorted_nums[1:]:
            if num - 1 == check_element:
                longest += 1
                check_element = num
            else:
                max_length = max(max_length, longest)
                longest = 1
                check_element = num
        
        return max(max_length, longest)