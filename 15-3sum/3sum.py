class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # final = []
        # for i, num in enumerate(nums):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     target = -1 * num
        #     left = i + 1
        #     right = len(nums) - 1
        #     while left < right:
        #         temp_target = nums[left] + nums[right]
                
        #         if temp_target > target:
        #             right -= 1
                
        #         elif temp_target < target:
        #             left += 1

        #         else:
        #             final.append([num, nums[left], nums[right]])
        #             left += 1

        #             while nums[left] == nums[left - 1] and left < right:
        #                 left += 1
            
        # return final

        final = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * num
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    final.append([num, nums[l], nums[r]])
                    l += 1
                    #r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                    # while nums[r] == nums[r + 1] and l < r:
                    #     r -= 1

                elif nums[l] + nums[r] < target:
                    l += 1

                    # while nums[l] == nums[l - 1] and l < r:
                    #     l += 1

                else:
                    r -= 1

                    # while nums[r] == nums[r + 1] and l < r:
                    #     r -= 1
        
        return final


        # final = []
        # for i, num in enumerate(nums):
        #     target = -1 * num
        #     map_dict = {}
        #     for new_num in nums[i+1:]:
        #         temp_target = target - new_num
        #         if temp_target not in map_dict:
        #             map_dict[new_num] = new_num
        #         else:
        #             temp = [num, new_num, temp_target]
        #             temp.sort()
        #             if temp not in final:
        #                 final.append(temp)
        
        # return final