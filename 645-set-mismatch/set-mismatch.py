class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        expec_sum = (l * (l + 1)) // 2
        curr_sum = sum(nums)
        unique_sum = sum(set(nums))

        return [curr_sum - unique_sum, expec_sum - unique_sum]
        # final = {}
        # result = []
        # for num in nums:
        #     if num not in final:
        #         final[num] = 1
        #     else:
        #         result.append(num)

        # for i in range(len(nums)):
        #     if i + 1 not in final:
        #         result.append(i+1)
        #         return result
