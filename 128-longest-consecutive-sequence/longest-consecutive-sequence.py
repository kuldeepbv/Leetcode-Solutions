class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                longest = 1
                while num + longest in num_set:
                    longest += 1
                max_length = max(max_length, longest)
            
        return max_length



            
        #     if num - 1 in nums and num + 1 not in nums:
        #         max_length = max(max_length, longest + 1)
        #         longest = 1
        #     else:
        #         longest += 1
                
        # return max(max_length, longest)

        # nums = set(nums)
        # sorted_nums = sorted(nums)
        # max_length = 0
        # check_element = sorted_nums[0]
        # longest = 1

        # for num in sorted_nums[1:]:
        #     if num - 1 == check_element:
        #         longest += 1
        #         check_element = num
        #     else:
        #         max_length = max(max_length, longest)
        #         longest = 1
        #         check_element = num
        
        # return max(max_length, longest)