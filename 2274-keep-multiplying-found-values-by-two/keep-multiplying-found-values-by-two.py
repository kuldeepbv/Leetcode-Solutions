class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original = 2 * original
        return original

        # while True:
        #     if original in nums:
        #         original = 2 * original
        #     else:
        #         return original