class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        final = []
        start = nums[0]
        temp = start
        for i, num in enumerate(nums[1:]):
            if i == len(nums) - 2:
                if num == temp + 1:
                    final.append(str(start) + '->' + str(num))
                    break
                else:
                    if nums[i] == start:
                        final.append(str(start))
                    else:
                        final.append(str(start) + '->' + str(nums[i]))
                    final.append(str(num))
                    break
            if num == temp + 1:
                temp = num
                continue
            else:
                if nums[i] == start:
                    final.append(str(start))
                else:
                    final.append(str(start) + '->' + str(nums[i]))
                start = num
                temp = start

        return final