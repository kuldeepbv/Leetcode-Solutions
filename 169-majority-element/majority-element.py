class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
        # count = {}
        # for num in nums:
        #     if num not in count.keys():
        #         count[num] = 1
        #     else:
        #         count[num] += 1
        
        # for key, value in count.items():
        #     if value > (len(nums) / 2):
        #         return key