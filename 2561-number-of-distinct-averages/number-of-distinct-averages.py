class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        ans = []
        while len(nums) > 0:
            avg = (max(nums) + min(nums)) / 2
            if avg not in ans:
                ans.append(avg)
            nums.remove(max(nums))
            nums.remove(min(nums))
        return len(ans)