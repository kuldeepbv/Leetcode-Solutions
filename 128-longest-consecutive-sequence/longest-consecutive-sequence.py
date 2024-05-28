class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums = sorted(nums)
        final_dict = {}

        if len(nums) == 0:
            count = 0
            return count
        else:
            count = 1

        for i in range(len(nums)):
            if i != len(nums) - 1:
                if nums[i+1] == nums[i] + 1 :
                    count += 1
                else:
                    final_dict[i] = count 
                    count = 1
            else:
                final_dict[i] = count 

        counts = list(final_dict.values())
        
        if counts:
            max_count = max(counts)
        else:
            max_count = 0

        return max_count