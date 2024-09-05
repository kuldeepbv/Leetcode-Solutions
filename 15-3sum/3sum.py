class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * num
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp_target = nums[left] + nums[right]
                
                if temp_target > target:
                    right -= 1
                
                elif temp_target < target:
                    left += 1

                else:
                    final.append([num, nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            
        return final
        #     while left < right:
        #         temp_target = nums[left] + nums[right]
        #         if temp_target == target:
        #             temp = [num, nums[left], nums[right]]
        #             temp.sort
        #             if temp not in final:
        #                 final.append(temp)
        #             left += 1
        #             right -= 1
        #             while left < right and nums[left] == nums[left-1]:
        #                 left += 1
        #             while left < right and nums[right] == nums[right+1]:
        #                 right -= 1
        #         elif temp_target < target:
        #             left += 1
        #         else:
        #             right -= 1

        # return final