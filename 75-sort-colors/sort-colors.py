class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_count = {0: 0, 1: 0, 2: 0}

        for num in nums:
            num_count[num] += 1

        idx = 0
        for num in num_count:
            while num_count.get(num, 0) > 0:
                nums[idx] = num
                idx += 1
                num_count[num] -= 1