class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        check = {}
        for num in nums:
            if num not in check.keys():
                check[num] = 1
            else:
                check[num] += 1
        
        for key, value in check.items():
            if value > (n / 2):
                return key