class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        final = nums
        for i in range(len(nums)):
            final.append(nums[i])
        return final