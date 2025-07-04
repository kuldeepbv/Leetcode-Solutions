class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # if len(nums) == 3:
        #     return sum(nums)

        # nums.sort()
        # check = sum(nums[:3])
        
        # for i in range(len(nums)-2):
        #     l = i + 1
        #     r = len(nums) - 1
        #     while l < r:
        #         curr_sum = nums[i] + nums[l] + nums[r]
        #         if abs(curr_sum - target) < abs(check - target):
        #             check = curr_sum
                
        #         if curr_sum == target:
        #             return curr_sum
        #         elif curr_sum < target:
        #             l += 1
        #         else:
        #             r -= 1
        
        # return check

        nums.sort()

        closest_sum = sum(nums[:3])

        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1
                else:
                    return current_sum

        return closest_sum                