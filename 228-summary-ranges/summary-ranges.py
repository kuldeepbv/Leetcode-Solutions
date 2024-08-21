class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # final = []
        # i = 0

        # while i < len(nums):
        #     start = nums[i]  
        #     while i < len(nums)-1 and nums[i] + 1 == nums[i + 1]: 
        #         i += 1 
            
        #     if start != nums[i]: 
        #         ans.append(str(start) + "->" + str(nums[i]))
        #     else: 
        #         ans.append(str(nums[i]))
            
        #     i += 1

        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        final = []
        start = nums[0]
        for i, num in enumerate(nums[1:]):
            if i == len(nums) - 2:
                if num == nums[i] + 1:
                    final.append(str(start) + '->' + str(num))
                    break
                else:
                    if nums[i] == start:
                        final.append(str(start))
                    else:
                        final.append(str(start) + '->' + str(nums[i]))
                    final.append(str(num))
                    break
            if num == nums[i] + 1:
                continue
            else:
                if nums[i] == start:
                    final.append(str(start))
                else:
                    final.append(str(start) + '->' + str(nums[i]))
                start = num

        return final