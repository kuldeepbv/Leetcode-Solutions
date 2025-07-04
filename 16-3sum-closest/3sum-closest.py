class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        nums.sort()
        check = sum(nums[:3])
        
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if abs(curr_sum - target) < abs(check - target):
                    check = curr_sum
                
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1
        
        return check