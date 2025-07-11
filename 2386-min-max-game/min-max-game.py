class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        new_nums = [0] * int(len(nums) / 2) 
        j = 0
        while len(nums) > 1:
            if j % 2 == 0:
                new_nums[j] = min(nums[2 * j], nums[(2 * j) + 1])
            else:
                new_nums[j] = max(nums[2 * j], nums[(2 * j) + 1])
            j += 1
            if j == len(new_nums):
                nums = new_nums
                new_nums = [0] * int(len(nums) / 2)
                j = 0
        return nums[0]