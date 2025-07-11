class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        set_nums = list(set(nums))
        ans = 0
        num_count = {}
        for num in set_nums:
            if nums.count(num) % 2 == 0:
                ans += 1
            #num_count[num] = nums.count(num)
        return ans == len(set_nums)