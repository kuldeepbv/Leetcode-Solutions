class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = []
        for i in range(len(nums)):
            for j in nums[i+1:]:
                if nums[i] + j == target:
                    final.append(i)
                    final.append((nums[i+1:].index(j)) + (i+1))
                    break
        return final