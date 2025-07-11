class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            for next_num in nums[i+1:]:
                if abs(nums[i] - next_num) == k:
                    ans += 1
        return ans