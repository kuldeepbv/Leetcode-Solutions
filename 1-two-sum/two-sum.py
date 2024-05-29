class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = []
        for i in range(len(nums)):
            next_num = target - nums[i]
            if next_num in nums[i+1:]:
                final.append(i)
                final.append((nums[i+1:].index(next_num)) + (i+1))
                break
        return final