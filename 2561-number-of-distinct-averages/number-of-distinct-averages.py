class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        ans = set()
        while l < r:
            avg = (nums[l] + nums[r]) / 2
            ans.add(avg)
            l += 1
            r -= 1
        return len(ans)