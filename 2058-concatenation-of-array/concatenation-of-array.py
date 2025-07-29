class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        j = 0
        for i in range(len(ans)):
            ans[i] = nums[j]
            j += 1
            if j == len(nums):
                j = 0
        return ans