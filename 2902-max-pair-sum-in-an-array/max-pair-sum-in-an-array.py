class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums_dict = {}

        for num in nums:
            max_dig = max(str(num))
            if max_dig in nums_dict:
                nums_dict[max_dig].append(num)
            else:
                nums_dict[max_dig] = [num]

        final = []

        for key, value in nums_dict.items():
            if len(value) >= 2:
                sorted_list = sorted(value, reverse = True)
                final.append(sorted_list[0] + sorted_list[1])

        if len(final) == 0:
            return -1
        else:
            return max(final)