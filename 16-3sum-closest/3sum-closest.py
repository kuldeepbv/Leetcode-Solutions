class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        final = 0
        check = float('inf')
        nums.sort()
        
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + num == target:
                    return target
                elif nums[l] + nums[r] + num < target:
                    if abs(nums[l] + nums[r] + num - target) < check:   
                        check = abs(nums[l] + nums[r] + num - target)
                        final = nums[l] + nums[r] + num

                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                else:
                    if abs(nums[l] + nums[r] + num - target) < check:   
                        check = abs(nums[l] + nums[r] + num - target)
                        final = nums[l] + nums[r] + num

                    r -= 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
        
        return final

                