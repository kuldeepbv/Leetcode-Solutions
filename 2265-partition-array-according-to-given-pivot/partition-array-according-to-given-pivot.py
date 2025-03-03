class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower_list = []
        middle_list = []
        upper_list = []

        for num in nums:
            if num < pivot:
                lower_list.append(num)
            elif num == pivot:
                middle_list.append(num)
            else:
                upper_list.append(num)
        
        return lower_list + middle_list + upper_list