class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        final = []
        for num in nums:
            final.append(num*num)
        return sorted(final)