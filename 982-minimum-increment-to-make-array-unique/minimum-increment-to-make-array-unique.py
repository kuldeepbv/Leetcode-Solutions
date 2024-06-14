class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        min_value = nums[0]
        count = 0

        for num in nums[1:]:
            if num <= min_value:
                count += (min_value + 1 - num)
                min_value += 1
            else:
                min_value = num
        
        return count