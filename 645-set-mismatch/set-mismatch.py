class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        final = {}
        result = []
        for num in nums:
            if num not in final:
                final[num] = 1
            else:
                result.append(num)

        for i in range(len(nums)):
            if i + 1 not in final:
                result.append(i+1)
                return result
