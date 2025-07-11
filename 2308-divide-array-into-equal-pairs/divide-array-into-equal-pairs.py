class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        set_nums = list(set(nums))
        ans = 0
        for num in set_nums:
            if nums.count(num) % 2 == 0:
                ans += 1
        return ans == len(set_nums)